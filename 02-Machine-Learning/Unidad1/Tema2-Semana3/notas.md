# 02-Machine-Learning - U1 T2 S3

## Notas de clase

### 2. Tema 2: Principios de modelado y validación

El objetivo de este tema es entender cómo se construye un proyecto de aprendizaje automático de forma ordenada y cómo se evalúa si el modelo realmente funciona. No basta con entrenar un algoritmo; hay que seguir un flujo de trabajo, medir el desempeño y comprobar que el resultado generaliza a datos nuevos.

### 2.1 Flujo de un proyecto de aprendizaje automático

Un proyecto de ML suele seguir estas etapas:

1. Definir el problema.
2. Recolectar y entender los datos.
3. Limpiar y preparar la información.
4. Dividir los datos en entrenamiento y prueba.
5. Elegir el modelo.
6. Entrenar el modelo.
7. Validar y ajustar hiperparámetros.
8. Evaluar con métricas.
9. Desplegar o comunicar resultados.
10. Monitorear el desempeño con el tiempo.

**Idea central:** el flujo no es lineal en la práctica. Muchas veces se vuelve a etapas anteriores si los datos son malos, la métrica es baja o el modelo no generaliza.

#### Flujo resumido

| Etapa | Qué se hace | Por qué importa |
|------|-------------|-----------------|
| Definición del problema | Se establece qué se quiere predecir o clasificar | Evita construir un modelo para una meta ambigua |
| Exploración de datos | Se identifican patrones, errores y variables importantes | Permite entender la calidad del conjunto de datos |
| Preprocesamiento | Se tratan faltantes, ruido, escalado y codificación | Mejora la calidad de entrada al modelo |
| División de datos | Se separan datos de entrenamiento, validación y prueba | Evita evaluar con datos ya vistos |
| Entrenamiento | El algoritmo aprende relaciones a partir de ejemplos | Construye el modelo |
| Validación | Se ajustan parámetros y se comparan alternativas | Ayuda a elegir el mejor modelo |
| Evaluación | Se miden métricas sobre datos nuevos | Indica desempeño real |
| Despliegue | Se usa el modelo en un contexto real | Convierte el modelo en una solución útil |

#### Conceptos clave del flujo

- **Datos de entrenamiento:** sirven para aprender patrones.
- **Datos de validación:** ayudan a ajustar el modelo sin tocar el conjunto final.
- **Datos de prueba:** se usan una sola vez para estimar el desempeño final.
- **Hiperparámetros:** son configuraciones del modelo que se ajustan manualmente o mediante búsqueda.
- **Generalización:** capacidad del modelo de funcionar bien con datos nuevos.

### 2.2 Métricas de desempeño: accuracy, precision, recall, F1-score, RMS

Las métricas sirven para cuantificar qué tan bien trabaja un modelo. La elección de la métrica depende del problema.

#### Matriz de confusión

Para problemas de clasificación binaria se usan cuatro resultados posibles:

| Resultado real | Predicción positiva | Predicción negativa |
|----------------|---------------------|---------------------|
| Positivo | Verdadero positivo (VP) | Falso negativo (FN) |
| Negativo | Falso positivo (FP) | Verdadero negativo (VN) |

#### Accuracy

Mide el porcentaje total de aciertos.

$$
Accuracy = \frac{VP + VN}{VP + VN + FP + FN}
$$

**Uso:** útil cuando las clases están balanceadas.

**Cuidado:** puede engañar si una clase domina el conjunto de datos.

#### Precision

Indica cuántos de los casos que el modelo marcó como positivos realmente lo eran.

$$
Precision = \frac{VP}{VP + FP}
$$

**Uso:** importante cuando un falso positivo es costoso.

Ejemplo: detectar spam. Si el modelo marca un correo importante como spam, eso puede ser un error serio.

#### Recall

Mide cuántos positivos reales logró detectar el modelo.

$$
Recall = \frac{VP}{VP + FN}
$$

**Uso:** importante cuando un falso negativo es costoso.

Ejemplo: detección médica. No detectar una enfermedad puede ser más grave que generar una alarma falsa.

#### F1-score

Combina precision y recall en una sola métrica.

$$
F1 = 2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}
$$

**Uso:** útil cuando hay desbalance de clases y se quiere equilibrio entre precision y recall.

#### RMS

En el contexto de ML, RMS suele referirse al **Root Mean Square Error (RMSE)**, una métrica de error para regresión.

$$
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}
$$

Donde:
- $y_i$ es el valor real.
- $\hat{y}_i$ es el valor predicho.
- $n$ es el número de observaciones.

**Interpretación:** mientras más bajo sea el RMSE, mejor ajusta el modelo.

#### Comparación rápida de métricas

| Métrica | Tipo de problema | Qué mide | Cuándo usarla |
|--------|------------------|----------|---------------|
| Accuracy | Clasificación | Aciertos totales | Clases balanceadas |
| Precision | Clasificación | Calidad de las predicciones positivas | Cuando los falsos positivos importan |
| Recall | Clasificación | Cobertura de los positivos reales | Cuando los falsos negativos importan |
| F1-score | Clasificación | Balance entre precision y recall | Datos desbalanceados |
| RMSE | Regresión | Error promedio de predicción | Cuando se predicen valores numéricos |

### Puntos que suelen preguntar en quiz

- Accuracy no siempre es la mejor métrica.
- Precision y recall responden a tipos distintos de error.
- F1-score es útil cuando hay desbalance.
- RMSE se usa más en regresión que en clasificación.
- La validación evita que el modelo se evalúe con datos que ya vio.

## Quiz

### Pregunta 1: Orden correcto de un proyecto de ML

**Pregunta:** ¿Cuál es una secuencia razonable en un proyecto de aprendizaje automático?

**Opciones:**
- ❌ Entrenar primero y después definir el problema.
- ✅ **Definir el problema, preparar los datos, entrenar, validar y evaluar.**
- ❌ Evaluar antes de dividir los datos.

**Respuesta correcta:** Definir el problema, preparar los datos, entrenar, validar y evaluar.

**Por qué:** el proyecto debe seguir una lógica que comience por entender la necesidad y termine con una evaluación confiable.

### Pregunta 2: Accuracy

**Pregunta:** ¿Qué mide el accuracy?

**Opciones:**
- ✅ **El porcentaje total de aciertos.**
- ❌ Solo los errores del modelo.
- ❌ La relación entre falsos positivos y falsos negativos.

**Por qué:** accuracy compara aciertos totales frente al total de casos.

### Pregunta 3: Precision

**Pregunta:** ¿Cuándo es más útil la precision?

**Opciones:**
- ✅ **Cuando un falso positivo es costoso.**
- ❌ Cuando solo importa encontrar todos los positivos.
- ❌ Cuando se trabaja exclusivamente con regresión.

**Por qué:** precision penaliza las predicciones positivas incorrectas.

### Pregunta 4: Recall

**Pregunta:** ¿Qué representa el recall?

**Opciones:**
- ❌ La proporción de predicciones correctas totales.
- ✅ **La proporción de positivos reales detectados por el modelo.**
- ❌ La media de los valores predichos.

**Por qué:** recall mide cobertura sobre los casos positivos verdaderos.

### Pregunta 5: F1-score

**Pregunta:** ¿Por qué usar F1-score?

**Opciones:**
- ✅ **Porque equilibra precision y recall.**
- ❌ Porque solo funciona con regresión.
- ❌ Porque ignora los falsos positivos.

**Por qué:** F1 resume dos métricas complementarias en un solo valor.

### Pregunta 6: RMS o RMSE

**Pregunta:** ¿En qué tipo de problema se usa RMSE?

**Opciones:**
- ❌ Clasificación binaria.
- ✅ **Regresión.**
- ❌ Clustering sin etiquetas.

**Por qué:** RMSE mide error en variables numéricas continuas.

### Preguntas extraídas de los quizzes de la carpeta Quiz (con respuestas)

1. **Un ejemplo de métrica primaria en clasificación desbalanceada es:**
   - a. MAE
   - b. F1-score ✓
   - c. Accuracy

2. **¿Qué significa un modelo con accuracy = 0.95 en dataset muy desbalanceado (95% negativos)?**
   - a. Puede estar ignorando casi todos los positivos ✓
   - b. Clasifica bien ambas clases
   - c. Tiene recall perfecto

3. **En regresión, ¿qué mide el MAE?**
   - a. Error cuadrático medio
   - b. Promedio de errores absolutos ✓
   - c. Proporción de varianza explicada

4. **Si un modelo tiene recall = 1.0, significa que:**
   - a. Detecta todos los positivos reales ✓
   - b. No tiene falsos negativos
   - c. No tiene falsos positivos

5. **Un modelo con recall = 0.9 y precision = 0.3 indica que:**
   - a. Captura pocos positivos y muchos negativos
   - b. Detecta la mayoría de positivos, pero se equivoca mucho en los falsos positivos ✓
   - c. Tiene alta accuracy

6. **En curva ROC, el eje Y representa:**
   - a. Falsos positivos
   - b. Especificidad
   - c. Verdaderos positivos (recall/sensibilidad) ✓

7. **¿Qué métrica es más adecuada cuando los falsos positivos son muy costosos?**
   - a. R²
   - b. Precision ✓
   - c. Recall

8. **¿Cuál es el propósito principal de la trazabilidad en el ciclo de vida de un modelo de ML?**
   - a. Aumentar la velocidad de entrenamiento
   - b. Documentar y verificar decisiones y riesgos ✓
   - c. Reducir el tamaño del dataset

9. **En triage hospitalario, si la prioridad es no perder urgentes, se debe maximizar:**
   - a. MAE
   - b. Recall ✓
   - c. Precision

10. **Un AUC cercano a 0.5 indica:**
	- a. Modelo perfecto
	- b. Modelo aleatorio ✓
	- c. Modelo excelente

11. **En una matriz de confusión, los falsos negativos son:**
	- a. Negativos detectados como positivos
	- b. Casos positivos que el modelo clasificó como negativos ✓
	- c. Positivos detectados correctamente

12. **¿Qué función se relaciona con mapear riesgos y supuestos en el diseño?**
	- a. MANAGE
	- b. MEASURE
	- c. MAP ✓

13. **En regresión, ¿qué describe mejor el error absoluto medio (MAE)?**
	- a. Promedio de desviaciones absolutas respecto a la realidad ✓
	- b. Penaliza cuadráticamente errores
	- c. Proporción explicada de la varianza

14. **¿Qué ocurre con el recall si aumentan los falsos negativos?**
	- a. Se mantiene igual
	- b. Aumenta
	- c. Disminuye ✓

15. **La validación cruzada estratificada se recomienda cuando:**
	- a. Se trata de regresión
	- b. Las clases están desbalanceadas ✓
	- c. El dataset es grande

16. **¿Qué combinación refleja un modelo con alta precisión pero bajo recall?**
	- a. Muchos FN y pocos FP ✓
	- b. Muchos FP y pocos FN
	- c. Pocos FN y muchos FP

17. **Una ROC por encima de la diagonal indica:**
	- a. Rendimiento peor que el azar
	- b. Rendimiento mejor que el azar ✓
	- c. Un modelo siempre perfecto

18. **El recall es clave en un hospital cuando:**
	- a. No se puede perder ningún caso urgente ✓
	- b. Sobran recursos médicos
	- c. Los falsos positivos son muy costosos

19. **La fórmula del F1-score es:**
	- a. (Precision+Recall)/2
	- b. (VP+VN)/Total
	- c. 2(Precision x Recall)/(Precision+Recall) ✓

## Actividades

- [ ] Memorizar la secuencia completa del flujo de un proyecto de ML.
- [ ] Practicar las fórmulas de accuracy, precision, recall, F1 y RMSE.
- [ ] Resolver ejercicios de matriz de confusión sin ayuda.
- [ ] Explicar con tus palabras por qué accuracy puede ser engañoso.
- [ ] Identificar qué métrica conviene en un caso de spam, fraude y diagnóstico médico.


