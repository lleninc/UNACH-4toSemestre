# Unidad 3 — Resumen: Métodos en conjunto y ajuste de modelos

Resumen conciso de los temas 1.1–1.4 (basado en CA U3T1 CDIA-ML1.pdf).

## 1.1 Bagging, pasting y out-of-bag evaluation
- Bagging (Bootstrap Aggregating): entrenar múltiples modelos sobre
  subconjuntos muestreados con reemplazo y agregar (votación/promedio).
- Pasting: igual que bagging pero sin reemplazo (submuestras disjuntas).
- Objetivo: reducir la varianza de modelos inestables (p. ej. árboles).
- Out-of-Bag (OOB): evaluación interna usando las instancias no muestreadas
  en cada bootstrap — estima el error sin necesitar un conjunto de validación
  adicional.
- Ventajas: mejora la estabilidad y permite evaluación rápida con OOB.
- Desventajas: mayor coste computacional y menos ganancia si los modelos
  base ya son estables.

**Ejemplo (scikit-learn):**
```python
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
bag = BaggingClassifier(DecisionTreeClassifier(), n_estimators=50,
                        oob_score=True, random_state=42)
``` 

## 1.2 Random Forests y Extra-Trees
- Random Forests: ensemble de árboles entrenados sobre bootstraps y
  seleccionando aleatoriamente un subconjunto de características en cada
  división. Combina votación/promedio para predicción.
- Extra-Trees (Extremely Randomized Trees): además de seleccionar
  características aleatorias, elige umbrales de división aleatoriamente,
  acelerando el entrenamiento y aumentando la diversidad.
- Ventajas: reducen varianza, manejan bien datos tabulares y ofrecen
  medidas de importancia de variables.
- Diferencias clave: RF busca el mejor umbral por nodo; Extra-Trees usa
  umbrales aleatorios (más ruido pero más velocidad y diversidad).
- Hiperparámetros importantes: `n_estimators`, `max_features`, `max_depth`,
  `min_samples_split`.

## 1.3 Métodos de potenciación (Boosting): AdaBoost, Gradient Boosting, XGBoost
- Boosting entrena modelos secuencialmente; cada nuevo modelo corrige
  errores residuales de los anteriores.
- AdaBoost: repondera instancias mal clasificadas; suele usar stumps
  (árboles muy poco profundos) como modelos débiles.
- Gradient Boosting: ajusta nuevos estimadores para minimizar la pérdida
  mediante aproximación por gradiente (control por `learning_rate`).
- XGBoost: implementación optimizada de Gradient Boosting con
  regularización, paralelismo y mejoras de rendimiento; frecuente en
  competiciones por su eficiencia y precisión.
- Riesgos/consideraciones: alta capacidad de ajuste (overfitting) si no
  se regulariza; observar `learning_rate`, `n_estimators`, `max_depth`,
  y usar validación cruzada.

## 1.4 Stacking y Blending
- Stacking: apilar las predicciones de varios modelos base (nivel 0)
  y entrenar un meta-modelo (nivel 1) sobre esas predicciones. Usualmente
  se generan las entradas del meta-modelo mediante CV para evitar fugas.
- Blending: similar al stacking pero utiliza un conjunto de validación
  separado para producir las características del meta-modelo (más simple
  pero usa menos datos para entrenamiento).
- Ventajas: combina fuerzas de modelos heterogéneos; puede mejorar
  rendimiento final. Desventajas: mayor complejidad, riesgo de fuga de
  datos si no se usa CV correctamente.

---
Fuente: síntesis del material en `02-Machine-Learning/Unidad3/Tema1-Semana2/CA U3T1 CDIA-ML1.pdf`.
