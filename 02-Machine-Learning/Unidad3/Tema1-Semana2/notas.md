# 02-Machine-Learning - U3 T1 S2

## Notas de clase
### 1.2 Bosques Aleatorios (Random Forests) y Extra-Trees

- Random Forests: ensamblado de árboles de decisión entrenados sobre
	bootstraps del conjunto de datos y seleccionando aleatoriamente un
	subconjunto de características (`max_features`) en cada división del
	árbol. La combinación mediante votación o promedio reduce la varianza
	y mejora la generalización.

- Extra-Trees (Extremely Randomized Trees): similar a Random Forests pero
	con umbrales de división elegidos aleatoriamente (no se busca el mejor
	umbral). Esto acelera el entrenamiento y aumenta la diversidad entre
	los árboles.

- Ventajas: robustez frente al sobreajuste, medidas de importancia de
	características útiles para interpretabilidad, buen desempeño en datos
	tabulares.

- Parámetros clave: `n_estimators`, `max_features`, `max_depth`,
	`min_samples_split`, `random_state`.

**Ejemplo mínimo (scikit-learn):**
```python
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
et = ExtraTreesClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
et.fit(X_train, y_train)
```

## Quiz

## Actividades

