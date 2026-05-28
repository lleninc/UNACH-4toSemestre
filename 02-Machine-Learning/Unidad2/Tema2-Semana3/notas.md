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

### QUIZ: Machine Learning (QUIZ U2-T2-S3)

1. ¿Qué representan los nodos internos en un árbol de decisión?
	- a) Predicciones finales.
	- b) Condiciones de partición sobre variables. (Correcta)
	- c) Registros individuales de entrenamiento.
	- Correcta: b) Condiciones de partición sobre variables.
	- Por qué: Los nodos internos dividen el espacio de datos aplicando reglas (condiciones) sobre atributos; cada división separa subgrupos con distribuciones de clase más homogéneas.

2. ¿Qué efecto tiene la poda en un árbol de decisión?
	- a) Aumentar el número de nodos terminales.
	- b) Calcular de nuevo la entropía.
	- c) Reducir ramas innecesarias para mejorar generalización. (Correcta)
	- Correcta: c) Reducir ramas innecesarias para mejorar generalización.
	- Por qué: La poda elimina ramas que se ajustan al ruido del conjunto de entrenamiento, disminuyendo la varianza y mejorando el rendimiento en datos no vistos.

3. ¿Qué sucede con la capacidad de generalización de un árbol muy profundo?
	- a) Permanece igual.
	- b) Se incrementa siempre.
	- c) Se reduce al aprender ruido. (Correcta)
	- Correcta: c) Se reduce al aprender ruido.
	- Por qué: Un árbol muy profundo puede modelar ejemplos individuales (ruido), lo que produce sobreajuste y peor desempeño en nuevos datos.

4. ¿Cuál es el riesgo de no podar un árbol de decisión?
	- a) Eliminación de nodos homogéneos.
	- b) Reducción de sesgo.
	- c) Captura de ruido en los datos. (Correcta)
	- Correcta: c) Captura de ruido en los datos.
	- Por qué: Sin poda el árbol conserva ramas que reflejan excepciones o ruido, incurriendo en complejidad innecesaria.

5. ¿Qué tipo de pregunta representa cada nodo interno de un árbol de decisión?
	- a) Una operación aritmética.
	- b) Un promedio ponderado.
	- c) Una condición sobre una variable. (Correcta)
	- Correcta: c) Una condición sobre una variable.
	- Por qué: Cada nodo formula una condición (por ejemplo, `x > t`) que decide la ruta hacia las hojas.

6. ¿Qué ocurre si un árbol es demasiado poco profundo?
	- a) Se subajusta. (Correcta)
	- b) Se sobreajusta.
	- c) No genera predicciones.
	- Correcta: a) Se subajusta.
	- Por qué: Si la profundidad es insuficiente, el modelo no captura patrones relevantes y tiene alto sesgo.

7. ¿Qué ocurre si se limita demasiado la profundidad de un árbol?
	- a) Puede perder patrones relevantes. (Correcta)
	- b) Mejora la generalización siempre.
	- c) La entropía se anula.
	- Correcta: a) Puede perder patrones relevantes.
	- Por qué: Limitar la profundidad impide representar relaciones complejas entre variables, reduciendo la capacidad predictiva.

8. ¿Qué criterio es computacionalmente más eficiente en la práctica?
	- a) El índice de Gini. (Correcta)
	- b) La entropía.
	- c) El promedio de clases.
	- Correcta: a) El índice de Gini.
	- Por qué: El índice de Gini suele requerir menos cálculo que la entropía (logaritmos), por eso es ligeramente más rápido en la práctica.

9. ¿Qué relación tienen los árboles de decisión con el sesgo y la varianza?
	- a) Siempre tienen alto sesgo.
	- b) Pueden regularse para equilibrar ambos. (Correcta)
	- c) Siempre tienen baja varianza.
	- Correcta: b) Pueden regularse para equilibrar ambos.
	- Por qué: Hiperparámetros como profundidad, `min_samples_leaf` y poda permiten ajustar sesgo/varianza según el problema.

10. ¿Qué representa un valor de Gini cercano a 0.5 en un nodo binario?
	- a) Un nodo eliminado por poda.
	- b) Un nodo muy mezclado. (Correcta)
	- c) Un nodo puro.
	- Correcta: b) Un nodo muy mezclado.
	- Por qué: En un nodo binario, Gini=0 indica pureza; valores cercanos a 0.5 muestran mezcla similar entre las dos clases.

### QUIZ: Revisión del intento (QUIZ U2-T2-S3)

1. ¿Qué significa que la entropía sea igual a 0 en un nodo?
	- a) El nodo contiene solo ejemplos positivos.
	- b) El nodo es completamente puro. (Correcta)
	- c) El nodo tiene incertidumbre máxima.
	- Correcta: b) El nodo es completamente puro.
	- Por qué: Entropía mide incertidumbre; 0 implica que todas las muestras pertenecen a la misma clase.

2. ¿Qué implica que un árbol tenga baja profundidad y alto error en entrenamiento?
	- a) Está sobreajustado.
	- b) Está subajustado. (Correcta)
	- c) Tiene baja varianza.
	- Correcta: b) Está subajustado.
	- Por qué: Baja profundidad limita la complejidad del modelo, impidiendo ajustar correctamente los datos de entrenamiento.

3. ¿Qué estrategia permite regular la complejidad de un árbol antes de crecer completamente?
	- a) Cálculo del error cuadrático medio.
	- b) Ajuste de hiperparámetros. (Correcta)
	- c) Aumento de hojas terminales.
	- Correcta: b) Ajuste de hiperparámetros.
	- Por qué: Ajustar hiperparámetros (p. ej. `max_depth`, `min_samples_split`) controla la complejidad durante el crecimiento.

4. ¿Qué refleja el dilema entre sesgo y varianza en árboles de decisión?
	- a) El método de optimización.
	- b) El equilibrio entre simplicidad y capacidad de generalización. (Correcta)
	- c) El número de variables predictoras.
	- Correcta: b) El equilibrio entre simplicidad y capacidad de generalización.
	- Por qué: Modelos simples (alto sesgo) no capturan complejidad; modelos complejos (alta varianza) sobreajustan. El objetivo es balancear ambos.

5. ¿Qué mide la entropía en un árbol de decisión?
	- a) La cantidad de nodos.
	- b) El número de divisiones realizadas.
	- c) El nivel de incertidumbre de la distribución de clases. (Correcta)
	- Correcta: c) El nivel de incertidumbre de la distribución de clases.
	- Por qué: La entropía cuantifica la impureza/aleatoriedad de las clases en un nodo.

6. ¿Qué significa que el índice de Gini sea cercano a 0?
	- a) La partición es heterogénea.
	- b) La partición es homogénea. (Correcta)
	- c) El árbol está sobreajustado.
	- Correcta: b) La partición es homogénea.
	- Por qué: Gini cercano a 0 indica que la mayoría de observaciones en el nodo pertenecen a la misma clase.

7. ¿Qué tipo de pregunta representa cada nodo interno de un árbol de decisión?
	- a) Una condición sobre una variable. (Correcta)
	- b) Una operación aritmética.
	- c) Un promedio ponderado.
	- Correcta: a) Una condición sobre una variable.
	- Por qué: Los nodos dividen según condiciones en atributos para separar clases.

8. ¿Cuál es el riesgo de no podar un árbol de decisión?
	- a) Eliminación de nodos homogéneos.
	- b) Captura de ruido en los datos. (Correcta)
	- c) Reducción de sesgo.
	- Correcta: b) Captura de ruido en los datos.
	- Por qué: Sin poda el árbol conserva divisiones que responden a variaciones aleatorias, empeorando la generalización.

9. ¿Qué puede suceder si se permite que los nodos de un árbol se dividan con muy pocas muestras?
	- a) El árbol se vuelve demasiado complejo y tiende a sobreajustar. (Correcta)
	- b) El modelo aumenta su sesgo de manera significativa.
	- c) El árbol se vuelve más general y sencillo.
	- Correcta: a) El árbol se vuelve demasiado complejo y tiende a sobreajustar.
	- Por qué: Dividir con pocas muestras crea ramas específicas a ejemplos particulares, elevando la varianza.

10. ¿Qué criterio es computacionalmente más eficiente en la práctica?
	- a) El índice de Gini. (Correcta)
	- b) El promedio de clases.
	- c) La entropía.
	- Correcta: a) El índice de Gini.
	- Por qué: Ver explicación arriba; Gini evita cómputos de logaritmos presentes en la entropía.

## Actividades

