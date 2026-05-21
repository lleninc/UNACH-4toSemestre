"""
Benchmarking de algoritmos metaheurísticos usando Boxplot

Este script carga (o genera) los datos experimentales de costo para
GA, PSO y ACO (10 ejecuciones cada uno), genera un diagrama de caja
y responde automáticamente las preguntas de análisis básicas.

Uso:
- Si dispone de un CSV llamado `datos_experimentales.csv` en la misma
  carpeta con columnas `GA`, `PSO`, `ACO`, el script lo usará.
- Si no existe, el script generará datos de ejemplo y los guardará.

Comentaré las partes más importantes tal como solicita la actividad.
"""
from pathlib import Path
import sys
import statistics as stats

DATA_FILE = Path(__file__).with_name("datos_experimentales.csv")
PLOT_FILE = Path(__file__).with_name("boxplot_benchmark.png")
HTML_FILE = Path(__file__).with_name("benchmark_report.html")

def ensure_packages():
    """Instala paquetes faltantes (si el entorno lo permite).

    Nota: esto intenta instalar dependencias automáticamente si no
    están presentes en el entorno virtual activo. Si no desea que el
    script instale paquetes, comente esta función y asegúrese de
    instalar manualmente: `pip install pandas matplotlib seaborn numpy`.
    """
    try:
        import pandas  # noqa: F401
        import matplotlib  # noqa: F401
        import seaborn  # noqa: F401
        import numpy  # noqa: F401
        import plotly  # noqa: F401
    except Exception:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "matplotlib", "seaborn", "numpy", "plotly"]) 


def load_or_generate_data():
    """Carga datos desde `datos_experimentales.csv` o genera ejemplo.

    El CSV esperado tiene columnas: GA, PSO, ACO con 10 filas cada una.
    Devuelve un diccionario con listas de valores.
    """
    import pandas as pd
    if DATA_FILE.exists():
        df = pd.read_csv(DATA_FILE)
        # Validar formato sencillo
        required = {"GA", "PSO", "ACO"}
        if not required.issubset(set(df.columns)):
            raise ValueError(f"CSV debe contener las columnas: {required}")
        return {alg: df[alg].dropna().tolist() for alg in ["GA", "PSO", "ACO"]}

    # Generar datos de ejemplo si no hay CSV
    import numpy as np
    rng = np.random.default_rng(12345)
    # Simulamos distintos comportamientos: medias y dispersión distintas
    ga = rng.normal(loc=1200, scale=80, size=10).round(2).tolist()
    pso = rng.normal(loc=1150, scale=50, size=10).round(2).tolist()
    aco = rng.normal(loc=1180, scale=150, size=10).round(2).tolist()

    # Guardar ejemplo para referencia
    df = pd.DataFrame({"GA": ga, "PSO": pso, "ACO": aco})
    df.to_csv(DATA_FILE, index=False)
    print(f"No se encontró CSV; se generó un ejemplo en: {DATA_FILE}")
    return {"GA": ga, "PSO": pso, "ACO": aco}


def detect_outliers_iqr(values):
    """Detecta outliers usando la regla IQR (1.5 * IQR).

    Devuelve una tupla: (lista_outliers, lower_bound, upper_bound)
    """
    import numpy as np
    a = np.array(values)
    q1 = np.percentile(a, 25)
    q3 = np.percentile(a, 75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outliers = a[(a < lower) | (a > upper)].tolist()
    return outliers, float(lower), float(upper)


def summarize_and_answer(data):
    """Calcula estadísticas y responde a las preguntas de la actividad.

    - Algoritmo con menor costo promedio
    - Algoritmo más estable (menor desviación estándar)
    - Algoritmo con mayor variabilidad
    - Posibles outliers
    - Recomendación
    """
    answers = {}
    stats_summary = {}
    for alg, vals in data.items():
        mean = stats.mean(vals)
        median = stats.median(vals)
        stdev = stats.pstdev(vals)  # desviación poblacional para comparar estabilidad
        q1 = None
        q3 = None
        try:
            import numpy as np
            q1 = float(np.percentile(vals, 25))
            q3 = float(np.percentile(vals, 75))
        except Exception:
            pass
        outliers, lower, upper = detect_outliers_iqr(vals)
        stats_summary[alg] = {
            "mean": mean,
            "median": median,
            "stdev": stdev,
            "q1": q1,
            "q3": q3,
            "outliers": outliers,
            "iqr_bounds": (lower, upper),
        }

    # Menor costo promedio
    best_mean_alg = min(stats_summary.items(), key=lambda x: x[1]["mean"])[0]
    # Más estable: menor stdev
    most_stable_alg = min(stats_summary.items(), key=lambda x: x[1]["stdev"])[0]
    # Mayor variabilidad: mayor stdev
    most_variable_alg = max(stats_summary.items(), key=lambda x: x[1]["stdev"])[0]

    answers["menor_costo_promedio"] = best_mean_alg
    answers["mas_estable"] = most_stable_alg
    answers["mayor_variabilidad"] = most_variable_alg
    answers["stats"] = stats_summary

    # Recomendación simple: preferir algoritmo con menor promedio y estabilidad razonable
    if best_mean_alg == most_stable_alg:
        recommendation = f"Recomendar {best_mean_alg}: mejor promedio y es el más estable."
    else:
        # comparar trade-off: si la diferencia de medias es pequeña, priorizar estabilidad
        mean_best = stats_summary[best_mean_alg]["mean"]
        mean_stable = stats_summary[most_stable_alg]["mean"]
        if (mean_stable - mean_best) / mean_best < 0.02:  # <2% diferencia
            recommendation = f"Aunque {best_mean_alg} tiene el menor promedio, {most_stable_alg} ofrece mayor estabilidad; elegir según prioridad (costo vs robustez)."
        else:
            recommendation = f"Recomendar {best_mean_alg} por menor costo promedio."

    answers["recomendacion"] = recommendation
    return answers


def plot_boxplot(data):
    """Genera y guarda el boxplot usando seaborn/matplotlib.

    Devuelve la ruta del archivo generado.
    """
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Convertir a formato long para seaborn
    df = pd.DataFrame(data)
    df_long = df.melt(var_name="Algoritmo", value_name="Costo")

    plt.figure(figsize=(8, 5))
    sns.boxplot(x="Algoritmo", y="Costo", data=df_long, palette="Set2")
    sns.swarmplot(x="Algoritmo", y="Costo", data=df_long, color="k", alpha=0.6)
    plt.title("Benchmark: comparación de costos por algoritmo (10 ejecuciones)")
    plt.ylabel("Costo total")
    plt.tight_layout()
    plt.savefig(PLOT_FILE, dpi=150)
    plt.close()
    return PLOT_FILE


def plotly_boxplot(data):
        """Crea un boxplot interactivo con Plotly y devuelve la figura.

        Usamos Plotly para generar una gráfica interactiva que se puede
        embeber en un HTML. También devolvemos la figura para incluirla
        en el informe.
        """
        import pandas as pd
        import plotly.express as px

        df = pd.DataFrame(data)
        df_long = df.melt(var_name="Algoritmo", value_name="Costo")

        fig = px.box(df_long, x="Algoritmo", y="Costo", points="all", color="Algoritmo",
                                 title="Benchmark: comparación de costos por algoritmo (10 ejecuciones)")
        fig.update_layout(showlegend=False)
        return fig


def generate_html_report(fig, data, answers):
        """Genera un HTML interactivo que contiene el plot y el resumen.

        El HTML incluye un resumen estadístico y la figura interactiva de
        Plotly. Se guarda en `benchmark_report.html`.
        """
        # Estadísticas en tabla HTML
        rows = []
        for alg, s in answers['stats'].items():
                rows.append(f"<tr><td>{alg}</td><td>{s['mean']:.2f}</td><td>{s['median']:.2f}</td><td>{s['stdev']:.2f}</td><td>{s['outliers']}</td></tr>")
        table_html = (
                "<table border=1 cellpadding=6><thead><tr><th>Algoritmo</th><th>Media</th><th>Mediana</th><th>Desviación</th><th>Outliers (IQR)</th></tr></thead>"
                + "<tbody>" + "".join(rows) + "</tbody></table>"
        )

        # Texto de preguntas/respuestas
        qa_html = (
                f"<p><b>Menor costo promedio:</b> {answers['menor_costo_promedio']}</p>"
                f"<p><b>Algoritmo más estable:</b> {answers['mas_estable']}</p>"
                f"<p><b>Algoritmo con mayor variabilidad:</b> {answers['mayor_variabilidad']}</p>"
                f"<p><b>Recomendación:</b> {answers['recomendacion']}</p>"
        )

        # Incrustar figura (fig.to_html devuelve un fragmento que incluye plotly.js si se solicita)
        fig_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

        html = f"""
        <html>
            <head>
                <meta charset='utf-8'>
                <title>Benchmark Report</title>
            </head>
            <body>
                <h1>Benchmark de algoritmos - Informe interactivo</h1>
                <h2>Resumen estadístico</h2>
                {table_html}
                <h2>Conclusiones</h2>
                {qa_html}
                <h2>Gráfica interactiva</h2>
                {fig_html}
            </body>
        </html>
        """

        HTML_FILE.write_text(html, encoding='utf-8')
        return HTML_FILE


def main():
    ensure_packages()
    data = load_or_generate_data()
    answers = summarize_and_answer(data)

    # Mostrar resumen en consola con comentarios útiles (en español)
    print("\n===== Resumen estadístico =====")
    for alg, s in answers["stats"].items():
        print(f"\n{alg}:")
        print(f"  Media: {s['mean']:.2f}")
        print(f"  Mediana: {s['median']:.2f}")
        print(f"  Desviación (poblacional): {s['stdev']:.2f}")
        print(f"  Outliers detectados (IQR): {s['outliers']}")

    print("\nPreguntas del enunciado:")
    print(f"- ¿Qué algoritmo obtuvo el menor costo promedio? -> {answers['menor_costo_promedio']}")
    print(f"- ¿Qué algoritmo parece ser más estable? -> {answers['mas_estable']}")
    print(f"- ¿Cuál algoritmo presenta mayor variabilidad? -> {answers['mayor_variabilidad']}")
    # Outliers aglutinados
    all_outliers = {alg: v['outliers'] for alg, v in answers['stats'].items()}
    print(f"- ¿Existe algún posible outlier? -> {all_outliers}")
    print(f"- Recomendación: {answers['recomendacion']}")

    # Graficar
    # Generar tanto la gráfica estática como la interactiva
    try:
        plot_path = plot_boxplot(data)
    except Exception:
        plot_path = None
    # Figura interactiva con Plotly
    fig = plotly_boxplot(data)
    report_path = generate_html_report(fig, data, answers)
    print(f"\nDiagrama (PNG) guardado en: {plot_path}")
    print(f"Informe interactivo guardado en: {report_path}")


if __name__ == "__main__":
    main()
