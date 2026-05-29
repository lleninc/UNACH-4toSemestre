# Resumen Unificado — Unidad 1: Fundamentos de Machine Learning

## Visión general
Breve introducción a Machine Learning (ML): disciplina que crea algoritmos capaces de aprender de datos para resolver tareas específicas sin reglas explícitas. El curso combina teoría, fundamentos matemáticos y prácticas con herramientas modernas (principalmente Python).

## Tipos de aprendizaje
- Supervisado: aprende desde datos etiquetados (clasificación, regresión).\
- No supervisado: descubre estructuras sin etiquetas (clustering, PCA).\
- Semi-supervisado: mezcla pocos etiquetados con mucho no etiquetado.\
- Por refuerzo: agentes que aprenden por interacción y recompensas.\
- Auto-supervisado: genera etiquetas desde los propios datos; base de LLMs.

## Aplicaciones y desafíos
- Áreas: salud (diagnóstico por imágenes), ingeniería civil/ambiental (deslizamientos, detección de fallas), telecom, educación personalizada, entre otras.
- Desafíos: sesgos y equidad, complejidad computacional (GPU/TPU y consumo), calidad de datos (ruido, nulos, no representatividad), interpretabilidad. Subcampos como XAI y Physics-Informed ML ayudan a mitigar estos retos.

## Fundamentos matemáticos
- Álgebra lineal: vectores, matrices, transformaciones, SVD/PCA.\
- Probabilidad: modelado de incertidumbre y procesos estocásticos (p. ej. Markov).\
- Estadística: inferencia, validación y pruebas para asegurar generalización.

## Herramientas
Ecosistema Python: NumPy, pandas, scikit-learn, matplotlib/seaborn, TensorFlow, PyTorch, Jupyter/Colab. MLOps para reproducibilidad y despliegue.

## Principios de modelado y validación
- Flujo típico: definir problema → preparar datos → engineering y modelado → evaluar/seleccionar → desplegar y monitorear.
- Gobernanza: trazabilidad, gestión de riesgos (NIST AI RMF), control de fugas de información, versionado y pipelines reproducibles.

## Métricas y decisiones de dominio
- Clasificación: accuracy, precision, recall, F1, AUROC/AUPRC; en desequilibrios, preferir F1/Recall/Balanced metrics.\
- Regresión: MAE, RMSE, R².\
- Calibración: log-loss, Brier, ECE cuando se usan probabilidades.
- Ajuste del umbral según costos de error del dominio (p. ej. priorizar recall en salud).

## Validación y robustez
- Dividir datasets correctamente (train/val/test), estratificar cuando convenga.\
- K-fold CV y CV anidada para tuning honesto.\
- Evitar data leakage: encapsular preprocesos dentro del pipeline de entrenamiento.

## Sobreajuste y mitigación
- Diagnóstico: curvas de aprendizaje y validación.\
- Técnicas: regularización L1/L2, early stopping, dropout, ensembles (bagging, boosting, stacking), manejo del desbalance (class weights, SMOTE, re-muestreo) dentro de CV.

## Recomendaciones prácticas
- Priorizar calidad de datos y diseño de validación reproducible.\
- Reportar métricas sensibles al dominio y documentar decisiones y supuestos.\
- Combinar técnicas (regularización + ensembles + validación correcta) para robustez.

---
Fuente: consolidación de "CA U1T1 CDIA-ML1.txt" y "CA U1T2 CDIA-ML1.txt" (Unidad 1, Tema 1 y Tema 2).

## Unidad 2 — Modelos avanzados de clasificación y regresión
Resumen: Unidad 2 profundiza en modelos lineales y no lineales, técnicas de regularización, máquinas de soporte vectorial (SVM), redes neuronales básicas y buenas prácticas de entrenamiento y selección de modelos.

- Modelos lineales y polinómicos: regresión lineal como base (solución matricial 𝛽̂=(X^T X)^{-1}X^T y), extensión polinómica para curvaturas; riesgo de sobreajuste al aumentar grado y necesidad de regularización.

- Regularización: Ridge (L2) penaliza la suma de cuadrados de coeficientes; Lasso (L1) penaliza sumas absolutas y puede inducir sparsidad (selección de variables). El hiperparámetro 𝜆 se ajusta con validación cruzada.

- Regresión logística y Softmax: función sigmoide para clasificación binaria; entropía cruzada (cross-entropy) como pérdida; Softmax generaliza a K clases entregando probabilidades que suman uno (capa de salida estándar en redes).

- Máquinas de Soporte Vectorial (SVM): buscan el hiperplano de máximo margen; reguladas por 𝐶 (trade-off margen/errores) y, con kernels (lineal, polinomial, RBF), permiten separar datos no lineales. En RBF, 𝛾 controla la influencia local de muestras (alto 𝛾→fronteras onduladas, bajo 𝛾→fronteras suaves). Ajustar 𝐶 y 𝛾 vía CV.

- Redes neuronales básicas (MLP): capas compuestas con activaciones (sigmoide, tanh, ReLU). Entrenamiento por retropropagación y optimizadores (SGD, Adam). Necesitan escalado de entradas y técnicas de regularización (weight decay, dropout, early stopping) para evitar sobreajuste.

- Optimización y buenas prácticas: normalizar/escala de features, usar validación cruzada anidada para tuning honesto, encapsular preprocesos en pipelines para evitar data leakage, y elegir modelos según tamaño/estructura de datos (SVM para conjuntos pequeños/medios, redes para grandes y complejos).

- Ensambles y robustez: bagging reduce varianza (Random Forest), boosting corrige sesgos (XGBoost/LightGBM), stacking combina modelos. Ensembles mejoran estabilidad pero requieren validación y control de fugas.

**Recomendación práctica Unidad 2:** empezar con modelos simples (regresión/Logistic/SVM) para establecer una línea base; escalar a redes o ensembles si los datos y el problema lo justifican; siempre validar con esquemas reproducibles y reportar métricas acordes al dominio.

---
Fuente adicional: "CA U2T1 CDIA-ML1.pdf" y "CA U2T2 CDIA-ML1.pdf" (Unidad 2, Tema 1 y Tema 2).