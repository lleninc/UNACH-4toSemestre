import warnings
warnings.filterwarnings('ignore')
import pandas as pd, numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression

root=Path(r'E:/Unach/Semestre4/EstudioGITClaude/UNACH-4toSemestre/04-Analitica-de-Datos/Unidad2/Tema1-Semana2/Autonomo')
RUTA_CSV = root / 'ant_datos_licencias_2022_mayo_hoja.csv'
print('CSV exists:', RUTA_CSV.exists())
raw = pd.read_csv(RUTA_CSV, sep=';', header=None, dtype=str, engine='python', encoding='utf-8')
TOKENS = {"A","A1","B","C","C1","D","E","F","G","TOTAL GENERAL","TOTAL_GENERAL","TOTALGENERAL"}

def score_header_row(row):
    vals = [str(x).strip().upper() for x in row.tolist()]
    hits = sum(v in TOKENS for v in vals)
    nstr = sum(v != "" for v in vals)
    return hits*1000 + nstr

hdr_idx = raw.apply(score_header_row, axis=1).idxmax()
header_vals = [str(x).strip() for x in raw.iloc[hdr_idx].tolist()]
if header_vals and (header_vals[0] == "" or header_vals[0].lower().startswith("unnamed")):
    header_vals[0] = "unidad"

cols_std = []
for c in header_vals:
    if pd.isna(c) or str(c).strip()=='' : cols_std.append('')
    else:
        s=str(c).strip().lower()
        s=s.replace('\n',' ').replace('\r',' ')
        s=s.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('ñ','n')
        s='_'.join(s.split())
        cols_std.append(s)

df_crudo = raw.iloc[hdr_idx+1:].copy()
try:
    df_crudo.columns = cols_std
except Exception as e:
    # pad
    diff = len(cols_std)-df_crudo.shape[1]
    if diff>0:
        for i in range(diff): df_crudo[i+df_crudo.shape[1]]=''
    df_crudo.columns = cols_std

if df_crudo.columns[0] != 'unidad':
    df_crudo = df_crudo.rename(columns={df_crudo.columns[0]:'unidad'})

cols_esperadas = ['unidad','a','a1','b','c','c1','d','e','f','g','total_general']
present = [c for c in cols_esperadas if c in df_crudo.columns]

df_crudo = df_crudo.loc[:, present]
clases_cols = [c for c in ['a','a1','b','c','c1','d','e','f','g'] if c in df_crudo.columns]
num_cols = clases_cols + (['total_general'] if 'total_general' in df_crudo.columns else [])

df_crudo = df_crudo.replace({"-": np.nan, '—':np.nan, '–':np.nan})
for c in num_cols:
    df_crudo[c] = (df_crudo[c].astype(str).str.replace(r"[^\d,\.\-]", '', regex=True).str.replace('.', '', regex=False).str.replace(',', '.', regex=False))
    df_crudo[c] = pd.to_numeric(df_crudo[c], errors='coerce')

if clases_cols:
    df_crudo[clases_cols] = df_crudo[clases_cols].fillna(0)
    suma_clases = df_crudo[clases_cols].sum(axis=1)
    if 'total_general' in df_crudo.columns:
        df_crudo['total_general'] = df_crudo['total_general'].fillna(suma_clases)
        dif = (df_crudo['total_general'] - suma_clases).abs()
        df_crudo.loc[dif > 0.5, 'total_general'] = suma_clases
    else:
        df_crudo['total_general'] = suma_clases
    df_crudo[num_cols] = df_crudo[num_cols].fillna(0).astype(int, errors='ignore')

report = {}
report['rows']=df_crudo.shape[0]
report['cols']=df_crudo.shape[1]
report['missing_pct'] = df_crudo.isna().mean().round(4).to_dict()
if 'total_general' in df_crudo.columns:
    suma = df_crudo[clases_cols].sum(axis=1)
    report['inconsistent_totals'] = int((df_crudo['total_general'] != suma).sum())
else:
    report['inconsistent_totals'] = None

# identify province summary rows
months = set(['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'])
def is_prov(x):
    if pd.isna(x): return False
    s=str(x).strip().lower()
    if s in months: return False
    return True
prov_mask = df_crudo['unidad'].apply(lambda x: is_prov(x))
prov_summary = df_crudo[prov_mask].copy()
prov_summary['prov_clean'] = prov_summary['unidad'].astype(str).str.strip().str.title()
agg_cols = clases_cols + ['total_general']
if not prov_summary.empty:
    prov_agg = prov_summary.groupby('prov_clean')[agg_cols].sum(min_count=1)
else:
    prov_agg = df_crudo.groupby('unidad')[agg_cols].sum(min_count=1)
prov_agg = prov_agg.sort_values('total_general', ascending=False)
for c in clases_cols:
    prov_agg[c+'_prop'] = (prov_agg[c] / prov_agg['total_general']).fillna(0)
prov_agg = prov_agg.reset_index()
if 'total_general' in prov_agg.columns:
    prov_agg['is_top'] = (prov_agg['total_general'] >= prov_agg['total_general'].quantile(0.75)).astype(int)
else:
    prov_agg['is_top'] = 0
X = prov_agg[[c+'_prop' for c in clases_cols]] if clases_cols else pd.DataFrame()
y = prov_agg['is_top']
model_results = {}
if not X.empty and y.nunique()>1:
    clf = LogisticRegression(max_iter=1000)
    cv = StratifiedKFold(n_splits=4, shuffle=True, random_state=42)
    from sklearn.model_selection import cross_val_score
    acc = cross_val_score(clf, X, y, cv=cv, scoring='accuracy')
    prec = cross_val_score(clf, X, y, cv=cv, scoring='precision', error_score='raise')
    rec = cross_val_score(clf, X, y, cv=cv, scoring='recall')
    f1 = cross_val_score(clf, X, y, cv=cv, scoring='f1')
    model_results = {'accuracy_mean': float(acc.mean()), 'precision_mean': float(prec.mean()), 'recall_mean': float(rec.mean()), 'f1_mean': float(f1.mean())}
else:
    model_results = {'note':'Insufficient features or single-class target to train model'}

out_pdf = root / 'Autonomo_resultados.pdf'
pp = PdfPages(out_pdf)
plt.figure(figsize=(8.27,11.69))
plt.axis('off')
txt = f"Autonomo: KDD aplicado - Resumen\nRows: {report['rows']} | Cols: {report['cols']}\nInconsistent totals: {report['inconsistent_totals']}\n\nModel results: {model_results}\n"
plt.text(0.01,0.99, txt, va='top', wrap=True)
pp.savefig(); plt.close()
plt.figure(figsize=(8,6))
prov_agg_sorted = prov_agg.sort_values('total_general', ascending=False).head(15)
plt.barh(prov_agg_sorted['prov_clean'][::-1], prov_agg_sorted['total_general'][::-1])
plt.title('Top 15 provincias por total general')
plt.tight_layout()
pp.savefig(); plt.close()
import seaborn as sns
plt.figure(figsize=(10,6))
if not prov_agg_sorted.empty:
    data = prov_agg_sorted[[c+'_prop' for c in clases_cols]].set_index(prov_agg_sorted['prov_clean'])
    sns.heatmap(data, annot=True, fmt='.2f', cmap='viridis')
    plt.title('Proporciones por categoria (top provincias)')
    plt.tight_layout()
    pp.savefig(); plt.close()
plt.figure(figsize=(8.27,11.69))
plt.axis('off')
tbl = prov_agg.head(30).to_string()
plt.text(0.01,0.99, tbl, va='top', family='monospace', wrap=True)
pp.savefig(); plt.close()
pp.close()
print('Wrote PDF:', out_pdf)
(root / 'autonomo_summary.json').write_text(str({'report':report,'model_results':model_results}))
print('Done')
