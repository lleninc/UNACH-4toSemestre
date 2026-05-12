# Autonomo 3 — KDD aplicado y comparación metodológica

**Archivo:** `ant_datos_licencias_2022_mayo_hoja.csv`

**Autor:** Apellido_Nombre (reemplazar)

---

## Pregunta 1 — ¿Qué es KDD y cuáles son sus cinco fases?

Respuesta:

KDD (Knowledge Discovery in Databases) es el proceso sistemático para extraer conocimiento útil y comprensible a partir de grandes volúmenes de datos. Sus cinco fases y propósitos son:

- Selección: elegir y reunir las fuentes y subconjuntos de datos relevantes para el problema (objetivo: disponer de la muestra correcta).
- Preprocesamiento: limpiar, estandarizar e imputar datos faltantes (objetivo: mejorar la calidad y consistencia de los datos).
- Transformación: generar variables, normalizar, codificar y reducir dimensionalidad cuando convenga (objetivo: adaptar los datos al método de minería).
- Minería: aplicar algoritmos (clustering, clasificación, regresión, reglas de asociación) para descubrir patrones (objetivo: extraer modelos o patrones cuantificables).
- Interpretación/evaluación: validar resultados, medir desempeño y traducir hallazgos a decisiones (objetivo: entregar conocimiento accionable).

Este flujo es necesario porque cada fase prepara el insumo para la siguiente; saltarse etapas provoca modelos pobres, fugas de información o conclusiones no replicables.

---

## Pregunta 2 — Clasificación de actividades por fase (con justificación breve)

a) Crear bitácora de calidad, detectar duplicados y estandarizar formatos de fecha.
- Fase: Preprocesamiento. Justificación: son tareas de limpieza y control de calidad necesarias antes de análisis.

b) Generar variables RFM y aplicar PCA.
- Fase: Transformación. Justificación: construcción de nuevas variables y reducción de dimensionalidad para preparar modelos.

c) Entrenar y comparar árboles de decisión, regresión logística y gradient boosting con validación cruzada.
- Fase: Minería. Justificación: aplicación y comparación de algoritmos predictivos para seleccionar el mejor modelo.

d) Definir la ventana temporal, fuentes autorizadas y criterios de inclusión/exclusión de registros.
- Fase: Selección. Justificación: determinación del conjunto de datos y límites temporales del estudio.

e) Elaborar un dashboard de hallazgos, explicar errores y proponer umbrales operativos.
- Fase: Interpretación. Justificación: comunicar resultados y convertir métricas en decisiones.

f) Imputar faltantes con reglas de negocio y KNN-imputer y documentar supuestos.
- Fase: Preprocesamiento. Justificación: imputación de valores faltantes y documentación de supuestos son tareas de limpieza y reproducibilidad.

---

## Pregunta 3 — Seis técnicas comunes en KDD (fase, herramienta sugerida, objetivo y entregable)

1. Muestreo estratificado — Fase: Selección — Herramienta: `scikit-learn` (`StratifiedKFold`) — Objetivo: preservar la distribución de clases — Entregable: conjunto de entrenamiento/validación estratificado.

2. Reglas de validación — Fase: Preprocesamiento — Herramienta: scripts `pandas` / `Great Expectations` — Objetivo: detectar y corregir inconsistencias — Entregable: bitácora de calidad.

3. One-hot encoding / scaling — Fase: Transformación — Herramienta: `pandas` / `scikit-learn` (`OneHotEncoder`, `StandardScaler`) — Objetivo: convertir variables categóricas y escalar números — Entregable: matriz de diseño lista para modelado.

4. PCA (reducción dimensional) — Fase: Transformación — Herramienta: `scikit-learn` (`PCA`) — Objetivo: reducir ruido y correlación entre variables — Entregable: componentes principales y gráfica de varianza explicada.

5. K-means (clustering) — Fase: Minería — Herramienta: `scikit-learn` (`KMeans`) — Objetivo: encontrar segmentos naturales — Entregable: etiquetas de clúster y perfil de segmentos.

6. Matriz de confusión / ROC — Fase: Interpretación — Herramienta: `scikit-learn` (`confusion_matrix`, `roc_auc_score`) — Objetivo: evaluar rendimiento predictivo — Entregable: tabla de métricas y curvas ROC.

---

## Pregunta 4 — Orden cronológico y fase asignada (justificación en una frase)

a) Definir la ventana “t-6 a t-1 meses” y listar tablas/variables autorizadas. — Fase: Selección. Justificación: define alcance temporal y fuentes.

b) Quitar outliers por IQR y normalizar montos. — Fase: Preprocesamiento. Justificación: limpiar y homogeneizar distribuciones antes de modelar.

c) Construir variables de “canasta” y lags semanales. — Fase: Transformación. Justificación: generar señales temporales y de comportamiento.

d) Comparar modelos y seleccionar el mejor por ROC-AUC y F1. — Fase: Minería. Justificación: evaluar y escoger el algoritmo más robusto.

e) Presentar un mapa de segmentos y reglas de acción para marketing. — Fase: Interpretación. Justificación: comunicar resultados aplicables.

f) Unir ventas internas con clima y calendario de promociones. — Fase: Selección / Transformación (preparación de fuentes externas). Justificación: integración de fuentes externas para enriquecer features.

---

## Ejercicio práctico (ANT) — Respuestas y resultados

Descripción del objetivo realizado: aplicar KDD al archivo `ant_datos_licencias_2022_mayo_hoja.csv` para limpieza, indicadores descriptivos, modelo de priorización provincial y traducción a acciones operativas.

### 1) Limpieza y documentación de calidad

- Procedimiento ejecutado: detección automática de la fila de encabezado, estandarización de nombres de columna, conversión numérica segura (eliminar separadores de miles y convertir coma decimal), reemplazo de símbolos `-` por NA, llenado de clases NaN con 0 y verificación/ajuste de `total_general` para que coincida con la suma de categorías.
- Resultados cuantitativos (resumen automático):

  - Filas procesadas: 504
  - Columnas: 11
  - Porcentaje de faltantes por columna: todas 0.0 según la limpieza automática
  - Totales inconsistentes detectados: 0 (se ajustaron donde fue necesario)

### 2) Indicadores descriptivos y visualizaciones

- Agregación a nivel provincial (suma por provincia de cada categoría y `total_general`).
- Indicadores entregados: totales por provincia, proporción por categoría (prop_*), y clasificación `is_top` (provincias en cuartil superior por `total_general`).
- Visualizaciones generadas (en `Autonomo_resultados.pdf`):
  - Barra horizontal con Top 15 provincias por `total_general`.
  - Heatmap de proporciones por categoría para las principales provincias.
  - Tabla con las primeras 30 provincias y sus totales.

### 3) Modelo de priorización provincial (enfoque y resultados)

- Target (definición): provincia `is_top` = 1 si `total_general` ≥ cuartil 75 (Top 25%); 0 en caso contrario.
- Features: proporciones por categoría (cada `c`/`total_general`), p. ej. `a_prop`, `b_prop`, etc.
- Algoritmo: regresión logística con validación cruzada estratificada (n_splits=4).
- Métricas reportadas (validación cruzada):

  - Accuracy (media CV): 0.75
  - Precision (media CV): 0.0
  - Recall (media CV): 0.0
  - F1 (media CV): 0.0

Notas sobre el modelo: los valores de precision/recall/f1 en 0.0 indican que, aunque la exactitud promedio es 0.75, el clasificador no identificó correctamente la clase positiva en los folds (probablemente por desequilibrio, pocos ejemplos positivos relativos o características predictoras débiles). Recomendaciones: aumentar muestras (agregando meses o fuentes), crear features adicionales (lags, tasas de crecimiento), o probar modelos no lineales (RandomForest, GradientBoosting) con calibración de umbral.

### 4) Traducción a decisiones operativas

- Priorización de provincias: usar el ranking por `total_general` y complementar con lift por categoría (`prop_*`) para definir focos (por ejemplo, priorizar provincias con alto share en categorías profesionales si la prioridad es servicios profesionales).
- Acciones tácticas propuestas:
  - Dimensionamiento: asignar recursos humanos temporales a provincias en Top 25% durante picos mensuales.
  - Especialización: fortalecer oficinas donde una categoría específica (ej. `B` o `C`) tenga un lift alto frente al promedio nacional.
  - Campañas: campañas de comunicación en provincias con alta proporción de solicitudes nuevas (emisión primera vez).

- Supuestos y límites: datos agregados (provincia×categoría×mes) impiden análisis a nivel oficina o individuo; resultados sensibles a errores de agregación; el modelo es indicativo, no prescriptivo.

---

## Bibliografía (estilo APA 7)

1. Han, J., Kamber, M., & Pei, J. (2012). Data Mining: Concepts and Techniques (3rd ed.). Morgan Kaufmann.

2. Fayyad, U., Piatetsky-Shapiro, G., & Smyth, P. (1996). From data mining to knowledge discovery in databases. AI Magazine, 17(3), 37–54.

3. Kuhn, M., & Johnson, K. (2019). Applied Predictive Modeling. Springer.

4. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). An Introduction to Statistical Learning. Springer.

5. Molnar, C. (2020). Interpretable Machine Learning. https://christophm.github.io/interpretable-ml-book/

---

### Archivos generados y reproducibilidad

- Script reproducible: `run_autonomo.py` (mismo directorio)
- Informe automático: `Autonomo_resultados.pdf`
- Resumen técnico: `autonomo_summary.json`

Reemplaza `Apellido_Nombre` por tu nombre antes de entregar.
