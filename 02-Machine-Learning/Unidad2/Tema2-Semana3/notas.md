# 02-Machine-Learning - U2 T2 S3

## Notas de clase

## Tema 2. Árboles de decisión y métricas avanzadas

### 2.1. Árboles de decisión: criterios de partición

- Un árbol de decisión divide el espacio de datos en regiones cada vez más homogéneas respecto a la variable objetivo.
- Cada nodo interno representa una pregunta o condición sobre una variable predictora.
- Cada hoja entrega una predicción: clase mayoritaria en clasificación o promedio en regresión.
- Los criterios de partición más usados son:
	- **Ganancia de información / entropía**: mide la reducción de incertidumbre al dividir los datos.
	- **Índice de Gini**: mide la impureza de la partición; cuanto menor es, más homogéneo es el nodo.
- En la práctica, Gini y entropía suelen dar resultados parecidos, pero Gini suele ser más eficiente computacionalmente.
- La profundidad del árbol controla su complejidad:
	- Un árbol muy profundo puede sobreajustar.
	- Un árbol muy poco profundo puede subajustar.
- Para equilibrar esto se usan poda y ajuste de hiperparámetros.

### 2.2. Métricas para multiclase

- La exactitud o accuracy por sí sola no es suficiente cuando las clases están desbalanceadas.
- Una matriz de confusión organiza los aciertos y errores en una tabla de tamaño $K \times K$.
- Métricas principales:
	- **Precision**: proporción de positivos correctos entre todos los predichos como positivos.
	- **Recall**: proporción de positivos correctos entre todos los positivos reales.
	- **F1-score**: media armónica entre precision y recall.
- Promedios usados en multiclase:
	- **Macro average**: trata todas las clases por igual.
	- **Weighted average**: pondera según el tamaño de cada clase.
	- **Micro average**: usa los conteos globales de la matriz.
- Métricas complementarias:
	- **ROC-AUC multiclase**: útil para evaluar discriminación entre clases.
	- **Kappa de Cohen**: corrige el acuerdo esperado por azar.
	- **Log-loss**: penaliza más las predicciones erróneas con alta confianza.

## Quiz

## Actividades

