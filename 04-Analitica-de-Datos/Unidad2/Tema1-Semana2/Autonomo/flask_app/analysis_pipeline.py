from __future__ import annotations

import base64
import io
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    make_scorer,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split


CSV_FILE = "ant_datos_licencias_2022_mayo_hoja.csv"
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent
CSV_PATH = DATA_DIR / CSV_FILE

TOKENS = {"A", "A1", "B", "C", "C1", "D", "E", "F", "G", "TOTAL GENERAL", "TOTAL_GENERAL", "TOTALGENERAL"}
MESES = {
    "ENERO",
    "FEBRERO",
    "MARZO",
    "ABRIL",
    "MAYO",
    "JUNIO",
    "JULIO",
    "AGOSTO",
    "SEPTIEMBRE",
    "OCTUBRE",
    "NOVIEMBRE",
    "DICIEMBRE",
}
PALABRAS_TIPO = ["DUPLICADO", "REIMPRES", "RECATEG", "PRIMERA VEZ", "RENOVAC", "EMISION"]
EXCLUDE_LABELS = {"TOTAL GENERAL", "TOTAL_GENERAL", "TOTALGENERAL"}
PROVINCIAS = {
    "AZUAY",
    "BOLIVAR",
    "CANAR",
    "CARCHI",
    "COTOPAXI",
    "CHIMBORAZO",
    "EL ORO",
    "ESMERALDAS",
    "GUAYAS",
    "IMBABURA",
    "LOJA",
    "LOS RIOS",
    "MANABI",
    "MORONA SANTIAGO",
    "NAPO",
    "PASTAZA",
    "PICHINCHA",
    "SANTA   ELENA",
    "SANTO   DOMINGO   DE   LOS   TSACHILAS",
    "SUCUMBIOS",
    "TUNGURAHUA",
    "ZAMORA CHINCHIPE",
    "GALAPAGOS",
    "ORELLANA",
}


def std_name(value: object) -> str:
    text = str(value).strip().replace("\n", " ").replace("\r", " ").lower()
    text = text.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ñ", "n")
    return "_".join(text.split())


def normaliza_txt(value: object) -> str:
    text = str(value).strip().upper()
    replacements = (("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"), ("Ú", "U"), ("Ü", "U"), ("Ñ", "N"))
    for old, new in replacements:
        text = text.replace(old, new)
    return " ".join(text.split())


def score_header_row(row: pd.Series) -> int:
    values = [str(item).strip().upper() for item in row.tolist()]
    hits = sum(value in TOKENS for value in values)
    non_empty = sum(value != "" for value in values)
    return hits * 1000 + non_empty


def resolve_csv_path() -> Path:
    if CSV_PATH.exists():
        return CSV_PATH

    candidates = list(DATA_DIR.glob(f"**/{CSV_FILE}"))
    if candidates:
        return candidates[0]

    raise FileNotFoundError(f"No se encontro {CSV_FILE} en {DATA_DIR}")


def load_crude_dataframe() -> pd.DataFrame:
    csv_path = resolve_csv_path()
    raw = pd.read_csv(csv_path, sep=";", header=None, dtype=str, engine="python", encoding="utf-8")

    header_index = raw.apply(score_header_row, axis=1).idxmax()
    header_values = [str(item).strip() for item in raw.iloc[header_index].tolist()]
    if header_values and (header_values[0] == "" or header_values[0].lower().startswith("unnamed")):
        header_values[0] = "unidad"

    columns = [std_name(column) for column in header_values]
    df = raw.iloc[header_index + 1 :].copy()
    df.columns = columns

    if df.columns[0] != "unidad":
        df = df.rename(columns={df.columns[0]: "unidad"})

    expected = ["unidad", "a", "a1", "b", "c", "c1", "d", "e", "f", "g", "total_general"]
    df = df.loc[:, [column for column in expected if column in df.columns]]

    numeric_columns = [column for column in ["a", "a1", "b", "c", "c1", "d", "e", "f", "g", "total_general"] if column in df.columns]
    df = df.replace({"-": np.nan, "—": np.nan, "–": np.nan})
    for column in numeric_columns:
        df[column] = (
            df[column]
            .astype(str)
            .str.replace(r"[^\d,\.\-]", "", regex=True)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
        )
        df[column] = pd.to_numeric(df[column], errors="coerce")

    class_columns = [column for column in ["a", "a1", "b", "c", "c1", "d", "e", "f", "g"] if column in df.columns]
    if class_columns:
        df[class_columns] = df[class_columns].fillna(0)
        class_sum = df[class_columns].sum(axis=1)
        if "total_general" in df.columns:
            df["total_general"] = df["total_general"].fillna(class_sum)
            diff = (df["total_general"] - class_sum).abs()
            df.loc[diff > 0.5, "total_general"] = class_sum
        else:
            df["total_general"] = class_sum

    if numeric_columns:
        df[numeric_columns] = df[numeric_columns].fillna(0).astype(int, errors="ignore")

    return df.reset_index(drop=True)


def build_province_tables(df_crudo: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    class_columns = [column for column in ["a", "a1", "b", "c", "c1", "d", "e", "f", "g"] if column in df_crudo.columns]
    dfN = df_crudo.copy()
    dfN["unidad_norm"] = dfN["unidad"].map(normaliza_txt)
    dfN["_n_num"] = dfN[class_columns].notna().sum(axis=1)

    mask_not_total = ~dfN["unidad_norm"].isin(EXCLUDE_LABELS)
    mask_cat = dfN["unidad_norm"].isin(PROVINCIAS)
    mask_mes = dfN["unidad_norm"].isin(MESES)
    mask_tipo = False
    for keyword in PALABRAS_TIPO:
        mask_tipo = mask_tipo | dfN["unidad_norm"].str.contains(keyword, na=False)

    mask_heur = (
        mask_not_total
        & ~mask_mes
        & ~mask_tipo
        & dfN["unidad_norm"].str.match(r"^[A-Z\s\.]+", na=False)
        & (dfN["unidad_norm"].str.len() <= 30)
        & (dfN["_n_num"] >= 3)
    )

    df_prov = dfN.loc[mask_cat | mask_heur, ["unidad"] + class_columns + (["total_general"] if "total_general" in dfN.columns else [])].copy()

    if "total_general" in df_prov.columns:
        df_prov["_tg"] = df_prov["total_general"].fillna(0)
        df_prov = (
            df_prov.assign(unidad_norm=df_prov["unidad"].map(normaliza_txt))
            .sort_values(["unidad_norm", "_tg"], ascending=[True, False])
            .drop_duplicates("unidad_norm", keep="first")
            .drop(columns=["unidad_norm", "_tg"])
            .reset_index(drop=True)
        )
    else:
        df_prov = (
            df_prov.assign(unidad_norm=df_prov["unidad"].map(normaliza_txt))
            .drop_duplicates("unidad_norm", keep="first")
            .drop(columns=["unidad_norm"])
            .reset_index(drop=True)
        )

    df_prov = df_prov.sort_values("unidad").reset_index(drop=True)
    return df_prov, dfN, class_columns


def build_long_table(df_prov: pd.DataFrame, class_columns: list[str]) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    dfp = df_prov.copy()
    dfp[class_columns] = dfp[class_columns].fillna(0)

    prov_long = dfp.melt(id_vars=["unidad"], value_vars=class_columns, var_name="clase", value_name="emisiones")
    prov_long["emisiones"] = pd.to_numeric(prov_long["emisiones"], errors="coerce").fillna(0).astype(int)

    tot_calc = prov_long.groupby("unidad", as_index=False)["emisiones"].sum().rename(columns={"emisiones": "total_calc"})
    df_prov2 = dfp.merge(tot_calc, on="unidad", how="left")
    if "total_general" in df_prov2.columns:
        diff = (df_prov2["total_general"].fillna(0) - df_prov2["total_calc"].fillna(0)).abs()
        df_prov2["_total"] = np.where(diff > 0.5, df_prov2["total_calc"], df_prov2["total_general"])
    else:
        df_prov2["_total"] = df_prov2["total_calc"]

    total_sum = df_prov2[class_columns].sum(axis=1).replace(0, np.nan)
    for column in class_columns:
        df_prov2[f"prop_{column}"] = (df_prov2[column] / total_sum).round(6)

    df_prov2 = df_prov2.sort_values("_total", ascending=False).reset_index(drop=True)
    return prov_long, tot_calc, df_prov2


def build_model(df_prov2: pd.DataFrame) -> dict:
    mix_cols = [column for column in df_prov2.columns if column.startswith("prop_")]
    score = df_prov2["_total"]
    q3 = score.quantile(0.75)
    y = (score >= q3).astype(int)

    min_pos = max(3, int(np.ceil(len(df_prov2) * 0.25)))
    if y.sum() < min_pos:
        idx_top = score.sort_values(ascending=False).head(min_pos).index
        y = pd.Series(0, index=score.index)
        y.loc[idx_top] = 1

    X = df_prov2[mix_cols].fillna(0)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)

    clf = RandomForestClassifier(n_estimators=200, class_weight="balanced", random_state=42, n_jobs=-1)
    clf.fit(Xtr, ytr)

    proba_te = clf.predict_proba(Xte)[:, 1]
    k_exp = max(1, int(round(ytr.mean() * len(yte))))
    order = np.argsort(-proba_te)
    pred_rank = np.zeros_like(yte)
    pred_rank[order[:k_exp]] = 1

    acc = accuracy_score(yte, pred_rank)
    prec = precision_score(yte, pred_rank, zero_division=0)
    rec = recall_score(yte, pred_rank, zero_division=0)
    f1 = f1_score(yte, pred_rank, zero_division=0)
    auc = roc_auc_score(yte, proba_te) if len(np.unique(yte)) == 2 else float("nan")

    n_splits = max(2, min(5, int(y.value_counts().min())))
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    scorers = {
        "accuracy": make_scorer(accuracy_score),
        "precision": make_scorer(precision_score, zero_division=0),
        "recall": make_scorer(recall_score, zero_division=0),
        "f1": make_scorer(f1_score, zero_division=0),
    }
    res = cross_validate(clf, X, y, cv=cv, scoring=scorers, n_jobs=-1)

    imp = pd.Series(clf.feature_importances_, index=mix_cols).sort_values(ascending=False).round(3)
    proba_all = clf.predict_proba(X)[:, 1]
    df_rank = df_prov2.assign(prob_top=proba_all).sort_values("prob_top", ascending=False).reset_index(drop=True)
    df_rank["pred_top_rank"] = 0
    topN_global = max(1, int(round(y.mean() * len(df_rank))))
    df_rank.loc[: topN_global - 1, "pred_top_rank"] = 1

    return {
        "mix_cols": mix_cols,
        "y": y,
        "split_metrics": {
            "accuracy": acc,
            "precision": prec,
            "recall": rec,
            "f1": f1,
            "roc_auc": auc,
            "confusion_matrix": confusion_matrix(yte, pred_rank),
            "classification_report": classification_report(yte, pred_rank, digits=3, zero_division=0),
        },
        "cv_metrics": pd.DataFrame({key: res[f"test_{key}"] for key in scorers}).agg(["mean", "std"]).round(3),
        "importance": imp,
        "ranked": df_rank,
    }


def figure_to_base64(fig: plt.Figure) -> str:
    buffer = io.BytesIO()
    fig.tight_layout()
    fig.savefig(buffer, format="png", dpi=160, bbox_inches="tight")
    plt.close(fig)
    return base64.b64encode(buffer.getvalue()).decode("ascii")


def plot_total_by_province(df_prov2: pd.DataFrame) -> str:
    fig, ax = plt.subplots(figsize=(12, 5))
    data = df_prov2.sort_values("_total", ascending=False).head(15)
    ax.bar(data["unidad"], data["_total"], color="#0f766e")
    ax.set_title("Emisiones por provincia (Top 15)")
    ax.set_xlabel("Provincia")
    ax.set_ylabel("Emisiones")
    ax.tick_params(axis="x", rotation=35, labelsize=8)
    return figure_to_base64(fig)


def plot_heatmap(df_matrix: pd.DataFrame, title: str, cmap: str = "viridis", color_label: str = "Valor") -> str:
    fig, ax = plt.subplots(figsize=(12, 7))
    image = ax.imshow(df_matrix.values, aspect="auto", cmap=cmap)
    fig.colorbar(image, ax=ax, label=color_label)
    ax.set_title(title)
    ax.set_yticks(range(len(df_matrix.index)))
    ax.set_yticklabels(df_matrix.index)
    ax.set_xticks(range(len(df_matrix.columns)))
    ax.set_xticklabels(df_matrix.columns)
    ax.tick_params(axis="x", rotation=35)
    return figure_to_base64(fig)


def build_dashboard() -> dict:
    df_crudo = load_crude_dataframe()
    df_prov, dfN, class_columns = build_province_tables(df_crudo)
    prov_long, tot_calc, df_prov2 = build_long_table(df_prov, class_columns)
    model = build_model(df_prov2)

    pivot_abs = (
        prov_long.pivot_table(index="unidad", columns="clase", values="emisiones", aggfunc="sum", fill_value=0)
        .reindex(df_prov2["unidad"])
    )
    fila_suma = pivot_abs.sum(axis=1).replace(0, np.nan)
    pivot_prop = (pivot_abs.div(fila_suma, axis=0)).fillna(0)

    prop_pais = pivot_abs.sum(axis=0) / pivot_abs.values.sum()
    lift = pivot_prop.div(prop_pais, axis=1).replace([np.inf, -np.inf], np.nan).fillna(0.0)
    var_pp = pivot_prop - prop_pais

    op_score = lift * df_prov2.set_index("unidad")["_total"].reindex(lift.index).values.reshape(-1, 1)
    top_lift = (
        op_score.stack()
        .reset_index()
        .rename(columns={"level_0": "unidad", "level_1": "clase", 0: "lift_pond"})
        .sort_values("lift_pond", ascending=False)
    )

    top15 = (
        top_lift.head(15)
        .merge(pivot_prop.stack().rename("prop_prov").reset_index(), on=["unidad", "clase"])
        .merge(prop_pais.rename("prop_pais").reset_index().rename(columns={"index": "clase"}), on="clase")
    )
    top15["lift"] = (top15["prop_prov"] / top15["prop_pais"]).round(2)
    top15["var_pp"] = (top15["prop_prov"] - top15["prop_pais"]).round(3)

    top_provinces = df_prov2[["unidad", "_total"]].head(10).copy()
    top_provinces["_total"] = top_provinces["_total"].astype(int)

    rank_preview = model["ranked"][ ["unidad", "_total", "prob_top", "pred_top_rank"] + model["mix_cols"] ].head(12).copy()
    rank_preview["prob_top"] = rank_preview["prob_top"].round(3)

    df_summary = pd.DataFrame(
        [
            [df_crudo.shape[0], df_crudo.shape[1], len(class_columns), int((df_prov2["_total"] < 0).sum())],
            [df_prov.shape[0], df_prov2.shape[0], len(top15), int(model["y"].sum())],
        ],
        columns=["filas", "columnas", "clases", "top_detectados"],
        index=["crudo", "provincias"],
    )

    if len(model["importance"]) >= 5:
        importance = model["importance"].head(5).reset_index()
        importance.columns = ["variable", "importancia"]
    else:
        importance = pd.DataFrame(columns=["variable", "importancia"])

    note_cards = [
        {"title": "Carga", "text": f"CSV detectado: {resolve_csv_path().name}"},
        {"title": "Limpieza", "text": f"Filas limpias: {df_crudo.shape[0]} y totales consistentes."},
        {"title": "Provincias", "text": f"Provincias detectadas: {df_prov2.shape[0]}."},
        {"title": "Modelo", "text": f"Accuracy test: {model['split_metrics']['accuracy']:.3f}."},
    ]

    return {
        "csv_path": str(resolve_csv_path()),
        "raw_shape": df_crudo.shape,
        "prov_shape": df_prov2.shape,
        "class_columns": class_columns,
        "summary_table": df_summary,
        "top_provinces": top_provinces,
        "df_prov2": df_prov2,
        "top_lift": top15,
        "rank_preview": rank_preview,
        "cv_metrics": model["cv_metrics"],
        "split_metrics": model["split_metrics"],
        "importance": importance,
        "charts": {
            "totals": plot_total_by_province(df_prov2),
            "heat_abs": plot_heatmap(pivot_abs, "Heatmap: provincia x clase (absoluto)", cmap="magma", color_label="Emisiones"),
            "heat_prop": plot_heatmap(pivot_prop, "Heatmap: provincia x clase (proporciones)", cmap="viridis", color_label="Proporción"),
        },
        "notes": note_cards,
    }
