# 02-Machine-Learning - U3 T1 S1

## Notas de clase
### 1.1 Bagging, Pasting y Out-of-Bag (OOB)

- Bagging (Bootstrap Aggregating): técnica de ensamblado que entrena
	múltiples modelos (por ejemplo, árboles de decisión) sobre muestras
	bootstrap (con reemplazo) del conjunto de datos y luego combina sus
	predicciones por votación (clasificación) o promedio (regresión). Reduce
	la varianza y mejora la estabilidad de modelos inestables.

- Pasting: variante que genera subconjuntos sin reemplazo. Útil cuando
	se quiere usar más de las observaciones sin repeticiones.

- Out-of-Bag (OOB) evaluation: en bagging, cada estimador se entrena con
	una muestra bootstrap; las observaciones no seleccionadas para un
	estimador concreto (aprox. 1/3 de los datos) pueden usarse para
	evaluar su rendimiento. El score OOB es una estimación interna del
	error de generalización sin necesidad de un conjunto de validación.

- Ventajas: sencillo de implementar, mejora la robustez y permite
	evaluación OOB rápida.
- Desventajas: mayor coste computacional y ganancias limitadas si los
	modelos base son ya muy estables.

**Ejemplo mínimo (scikit-learn):**
```python
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
bag = BaggingClassifier(DecisionTreeClassifier(), n_estimators=50,
												oob_score=True, random_state=42)
bag.fit(X_train, y_train)
print('OOB score:', bag.oob_score_)
```

## Quiz

## Actividades

