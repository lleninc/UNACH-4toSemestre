# 02-Machine-Learning - U2 T2 S4

## Notas de clase

## Tema 2. Modelos avanzados de clasificación y regresión

### 2.3. Interpretación y análisis de errores

- Entrenar un modelo no es suficiente; también hay que entender por qué se equivoca.
- El análisis de errores ayuda a detectar limitaciones del modelo, sesgos en los datos y oportunidades de mejora.
- En clasificación, los errores más importantes son:
	- **Falsos positivos (FP)**: el modelo predice positivo, pero la clase real es negativa.
	- **Falsos negativos (FN)**: el modelo predice negativo, pero la clase real es positiva.
- En regresión, los errores suelen analizarse con:
	- **MSE** (error cuadrático medio).
	- **MAE** (error absoluto medio).
	- Gráficos de residuos para detectar patrones sistemáticos.
- Interpretación clave:
	- Errores sistemáticos pueden indicar sesgo o un modelo demasiado simple.
	- Errores muy dispersos o aleatorios y altos pueden reflejar varianza alta y sobreajuste.
	- En problemas desbalanceados, una alta accuracy puede ser engañosa.

### 2.4. Aplicaciones prácticas en datasets reales

- El trabajo con datasets reales introduce ruido, valores faltantes y desbalance de clases.
- Casos de uso mencionados:
	- **Spam / detección de correo malicioso**: útil para estudiar desbalance y métricas como ROC-AUC.
	- **Salud / Heart Disease**: los falsos negativos son críticos porque pueden ocultar un diagnóstico real.
	- **Imágenes / MNIST o Fashion-MNIST**: permiten estudiar confusiones entre clases visualmente similares.
	- **Regresión / House Prices**: los residuos ayudan a ver si el modelo subestima precios altos o sigue un sesgo hacia el promedio.
- Usar datos reales conecta la teoría con aplicaciones en salud, finanzas y seguridad digital.
- El error no solo indica fallos: también revela cómo mejorar el modelo y qué límites tiene.

## Quiz

### QUIZ U2-T2-S4 (APE8) - Machine Learning

1. ¿Por qué la exactitud es engañosa en detección de fraudes?
	- a) Porque la clase fraudulenta es mayoritaria.
	- b) Porque no mide la precisión en tiempo real.
	- c) Porque un modelo puede predecir siempre "no fraude" y tener alta accuracy. (Correcta)
	- Correcta: c) Porque un modelo puede predecir siempre "no fraude" y tener alta accuracy.
	- Por qué: En problemas altamente desbalanceados la clase mayoritaria puede dominar la métrica, ocultando fallos en la clase minoritaria.

2. ¿Qué visión fomenta el análisis de errores en estudiantes?
	- a) Que solo importa el F1-score.
	- b) Una mirada crítica para evaluar limitaciones y mejoras. (Correcta)
	- c) Que los modelos son siempre exactos.
	- Correcta: b) Una mirada crítica para evaluar limitaciones y mejoras.
	- Por qué: Analizar errores enseña a identificar causas, sesgos y oportunidades de mejora, más allá de una sola métrica.

3. ¿Por qué se prioriza el recall en problemas médicos?
	- a) Porque es más grave no detectar un caso positivo que detectarlo erróneamente. (Correcta)
	- b) Porque siempre da valores más altos que la precisión.
	- c) Porque se busca minimizar la cantidad de predicciones negativas.
	- Correcta: a) Porque es más grave no detectar un caso positivo que detectarlo erróneamente.
	- Por qué: En salud, los falsos negativos pueden tener consecuencias severas; por eso se prioriza sensibilidad.

4. ¿Qué representa un falso negativo en un dataset de salud?
	- a) Diagnosticar correctamente la ausencia de enfermedad.
	- b) Detectar erróneamente enfermedad en un paciente sano.
	- c) No detectar enfermedad en un paciente que sí la tiene. (Correcta)
	- Correcta: c) No detectar enfermedad en un paciente que sí la tiene.
	- Por qué: Un falso negativo significa que el modelo clasificó como negativo un caso que es realmente positivo.

5. ¿Qué mide el recall (sensibilidad) para una clase?
	- a) La proporción de falsos positivos sobre el total de predicciones positivas.
	- b) La proporción de verdaderos positivos sobre todos los casos realmente positivos. (Correcta)
	- c) La proporción de predicciones correctas sobre el total de predicciones.
	- Correcta: b) La proporción de verdaderos positivos sobre todos los casos realmente positivos.
	- Por qué: El recall evalúa la capacidad del modelo para encontrar todos los casos positivos reales.

6. ¿Por qué la accuracy puede ser engañosa en un problema multiclase desbalanceado?
	- a) Porque un modelo puede acertar mayormente en clases frecuentes y fallar en las minoritarias. (Correcta)
	- b) Porque siempre da un valor bajo en cualquier escenario.
	- c) Porque solo mide los errores en la clase mayoritaria.
	- Correcta: a) Porque un modelo puede acertar mayormente en clases frecuentes y fallar en las minoritarias.
	- Por qué: Accuracy promedia aciertos sobre todas las clases, por lo que puede ocultar mal desempeño en clases pequeñas.

7. ¿Qué enseñan los errores en modelos de aprendizaje automático?
	- a) Que los errores pueden ser pistas para mejorar modelos y datos. (Correcta)
	- b) Que los algoritmos son siempre incorrectos.
	- c) Que las métricas no son necesarias.
	- Correcta: a) Que los errores pueden ser pistas para mejorar modelos y datos.
	- Por qué: Analizar patrones de error ayuda a identificar sesgos, features faltantes o problemas de etiquetado.

8. ¿Qué indica un patrón sistemático en los errores?
	- a) Posible sesgo en los datos o el modelo. (Correcta)
	- b) Varianza alta.
	- c) Aleatoriedad total en los errores.
	- Correcta: a) Posible sesgo en los datos o el modelo.
	- Por qué: Un patrón repetible sugiere que hay un factor sistemático que el modelo no captura.

9. ¿Qué son los falsos positivos (FP) en clasificación?
	- a) Casos correctamente clasificados en la clase positiva.
	- b) Casos predichos como negativos siendo positivos.
	- c) Casos predichos como positivos siendo negativos. (Correcta)
	- Correcta: c) Casos predichos como positivos siendo negativos.
	- Por qué: FP son instancias en que el modelo etiquetó como positivo a un caso que en realidad es negativo.

10. ¿Cómo puede mejorar un modelo con sesgo hacia precios bajos?
	- a) Eliminando la mitad de los datos.
	- b) Usando técnicas de regularización o nuevas variables. (Correcta)
	- c) Incrementando aleatoriamente los precios reales.
	- Correcta: b) Usando técnicas de regularización o nuevas variables.
	- Por qué: Regularización y features adicionales pueden reducir sesgos y capturar relaciones relevantes.

### QUIZ U2-T2-S4 (APE8) - ML_LL

1. ¿Por qué la exactitud es engañosa en detección de fraudes?
	- a) Porque la clase fraudulenta es mayoritaria.
	- b) Porque no mide la precisión en tiempo real.
	- c) Porque un modelo puede predecir siempre "no fraude" y tener alta accuracy. (Correcta)
	- Correcta: c) Porque un modelo puede predecir siempre "no fraude" y tener alta accuracy.
	- Por qué: En datasets con clases muy desbalanceadas, la clase mayoritaria puede dominar la métrica.

2. ¿Qué muestra un gráfico de residuos en regresión?
	- a) La tasa de falsos positivos y negativos.
	- b) La distribución de las clases por categoría.
	- c) La diferencia entre valores predichos y observados. (Correcta)
	- Correcta: c) La diferencia entre valores predichos y observados.
	- Por qué: Los residuos permiten detectar patrones sistemáticos y heterocedasticidad.

3. ¿Qué enseñan los errores en modelos de aprendizaje automático?
	- a) Que las métricas no son necesarias.
	- b) Que los errores pueden ser pistas para mejorar modelos y datos. (Correcta)
	- c) Que los algoritmos son siempre incorrectos.
	- Correcta: b) Que los errores pueden ser pistas para mejorar modelos y datos.
	- Por qué: Los errores informan sobre limitaciones en features, etiquetado o representatividad.

4. ¿Qué tipo de datasets suelen presentar ruido y valores faltantes?
	- a) Datasets sintéticos.
	- b) Datasets balanceados.
	- c) Datasets reales. (Correcta)
	- Correcta: c) Datasets reales.
	- Por qué: Los datos recolectados del mundo real tienden a tener errores, ruido y faltantes.

5. En regresión, ¿qué mide el error cuadrático medio (MSE)?
	- a) El porcentaje de errores de clasificación.
	- b) El promedio de las diferencias absolutas.
	- c) El promedio de los cuadrados de las diferencias entre predicciones y valores reales. (Correcta)
	- Correcta: c) El promedio de los cuadrados de las diferencias entre predicciones y valores reales.
	- Por qué: MSE penaliza errores grandes al elevar al cuadrado las diferencias.

6. ¿Qué rol tiene el análisis de residuos en predicción de precios de vivienda?
	- a) Ajustar automáticamente los hiperparámetros.
	- b) Ver la distribución de las etiquetas reales.
	- c) Identificar si el modelo subestima precios altos. (Correcta)
	- Correcta: c) Identificar si el modelo subestima precios altos.
	- Por qué: Los residuos muestran sesgos en distintas regiones del espacio de predicción.

7. ¿Qué son los falsos positivos (FP) en clasificación?
	- a) Casos correctamente clasificados en la clase positiva.
	- b) Casos predichos como positivos siendo negativos. (Correcta)
	- c) Casos predichos como negativos siendo positivos.
	- Correcta: b) Casos predichos como positivos siendo negativos.
	- Por qué: FP se refiere a predicciones positivas incorrectas.

8. ¿Qué visión fomenta el análisis de errores en estudiantes?
	- a) Que los modelos son siempre exactos.
	- b) Una mirada crítica para evaluar limitaciones y mejoras. (Correcta)
	- c) Que solo importa el F1-score.
	- Correcta: b) Una mirada crítica para evaluar limitaciones y mejoras.
	- Por qué: Ver explicación arriba.

9. ¿Qué penaliza el log-loss en clasificación?
	- a) Los errores de predicción con baja probabilidad.
	- b) Las predicciones incorrectas con alta confianza. (Correcta)
	- c) Los aciertos en clases mayoritarias.
	- Correcta: b) Las predicciones incorrectas con alta confianza.
	- Por qué: Log-loss castiga fuertemente predicciones erróneas realizadas con alta probabilidad.

10. ¿Cómo puede extenderse el ROC-AUC a problemas multiclase?
	- a) Usando el enfoque "uno contra todos" para cada clase. (Correcta)
	- b) Calculando un valor único de exactitud.
	- c) Promediando las matrices de confusión.
	- Correcta: a) Usando el enfoque "uno contra todos" para cada clase.
	- Por qué: El método uno-vs-all permite calcular AUC por clase y promediar o ponderar los resultados.

### QUIZ U2-T2-S4 (APE8) - ML_LL1

1. ¿Cómo funciona el weighted average en clasificación multiclase?
	- a) Usa el promedio de métricas más altas.
	- b) Ignora las clases con baja frecuencia.
	- c) Pondera cada clase según su proporción en el dataset. (Correcta)
	- Correcta: c) Pondera cada clase según su proporción en el dataset.
	- Por qué: Weighted average suma las métricas por clase ponderadas por soporte (número de instancias).

2. ¿Cómo puede mejorar un modelo con sesgo hacia precios bajos?
	- a) Usando técnicas de regularización o nuevas variables. (Correcta)
	- b) Incrementando aleatoriamente los precios reales.
	- c) Eliminando la mitad de los datos.
	- Correcta: a) Usando técnicas de regularización o nuevas variables.
	- Por qué: Ver explicación en sección anterior.

3. ¿Por qué se prioriza el recall en problemas médicos?
	- a) Porque se busca minimizar la cantidad de predicciones negativas.
	- b) Porque siempre da valores más altos que la precisión.
	- c) Porque es más grave no detectar un caso positivo que detectarlo erróneamente. (Correcta)
	- Correcta: c) Porque es más grave no detectar un caso positivo que detectarlo erróneamente.
	- Por qué: Ver explicación arriba.

4. ¿Cuál es la fórmula del F1-score?
	- a) F1=(Precisión+Recall)/2
	- b) F1=(Precisión-Recall)/(Precisión+Recall)
	- c) F1=2*(Precisión*Recall)/(Precisión+Recall) (Correcta)
	- Correcta: c) F1=2*(Precisión*Recall)/(Precisión+Recall).
	- Por qué: F1 es la media armónica entre precisión y recall.

5. ¿Qué son los falsos negativos (FN)?
	- a) Casos predichos como positivos siendo positivos.
	- b) Casos correctamente clasificados como negativos.
	- c) Casos predichos como negativos siendo positivos. (Correcta)
	- Correcta: c) Casos predichos como negativos siendo positivos.
	- Por qué: FN ocurre cuando el modelo no detecta una instancia positiva.

6. ¿Qué refleja el análisis de palabras mal clasificadas en spam?
	- a) Que algunos patrones lingüísticos inducen a error al modelo. (Correcta)
	- b) Que el modelo tiene varianza infinita.
	- c) Que el dataset no sirve.
	- Correcta: a) Que algunos patrones lingüísticos inducen a error al modelo.
	- Por qué: Los ejemplos mal clasificados muestran qué características confunden al clasificador.

7. ¿Qué indica un patrón sistemático en los errores?
	- a) Varianza alta.
	- b) Posible sesgo en los datos o el modelo. (Correcta)
	- c) Aleatoriedad total en los errores.
	- Correcta: b) Posible sesgo en los datos o el modelo.
	- Por qué: Repetición de un fallo apunta a un sesgo subyacente.

8. ¿Qué problema se observa en la detección de spam?
	- a) El desbalance entre spam y no spam. (Correcta)
	- b) El log-loss siempre es bajo.
	- c) Los correos legítimos siempre se clasifican como spam.
	- Correcta: a) El desbalance entre spam y no spam.
	- Por qué: El desbalance complica el aprendizaje y requiere técnicas de manejo de clases.

9. ¿Qué mide el índice Kappa de Cohen en clasificación?
	- a) El porcentaje de falsos positivos.
	- b) El tiempo de entrenamiento del modelo.
	- c) El grado de acuerdo entre predicciones y realidad corrigiendo por azar. (Correcta)
	- Correcta: c) El grado de acuerdo entre predicciones y realidad corrigiendo por azar.
	- Por qué: Kappa compara acuerdo observado con el esperado por azar.

10. ¿Qué mide el recall (sensibilidad) para una clase?
	- a) La proporción de falsos positivos sobre el total de predicciones positivas.
	- b) La proporción de verdaderos positivos sobre todos los casos realmente positivos. (Correcta)
	- c) La proporción de predicciones correctas sobre el total de predicciones.
	- Correcta: b) La proporción de verdaderos positivos sobre todos los casos realmente positivos.
	- Por qué: Repetición de la definición de sensibilidad.

## Actividades

