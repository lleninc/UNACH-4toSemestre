# Quiz Unificado — 02-Machine-Learning

1. Qué determina la clase predicha en Softmax?**
Source: notas.md
- a. El promedio de coeficientes
- b. La clase con probabilidad más alta ✓
- c. La suma de errores

2. Qué función se utiliza en la regresión logística binaria?**
Source: notas.md
- a. Sigmoide (logística) ✓
- b. Función identidad
- c. Tangente hiperbólica

3. Qué supone la regresión lineal sobre los errores?**
Source: notas.md
- a. Que sean independientes y homocedásticos ✓
- b. Que sigan una distribución uniforme
- c. Que siempre sean positivos

4. Cuál es el propósito principal de la regresión lineal?**
Source: notas.md
- a. Clasificar variables en categorías
- b. Estimar una variable de salida en función de predictores ✓
- c. Calcular probabilidades acumuladas

5. Qué función se utiliza en la regresión logística binaria?**
Source: notas.md
- a. Función identidad
- b. Sigmoide (logística) ✓
- c. Tangente hiperbólica

6. Qué papel cumple el parámetro b en la regresión logística?**
Source: notas.md
- a. El grado polinómico
- b. La tasa de aprendizaje
- c. El sesgo (bias o intercepto) ✓

7. Qué condición debe cumplir la matriz X para que la solución matricial de la regresión lineal sea posible?**
Source: notas.md
- a. Que todos los coeficientes sean positivos
- b. Que tenga rango completo ✓
- c. Que todos los residuos sean iguales a cero

8. Qué ocurre si la relación entre variables es no lineal y se usa regresión lineal simple?**
Source: notas.md
- a. El modelo ajusta perfectamente los datos
- b. El modelo presenta alto sesgo ✓
- c. El modelo mejora la varianza

9. Qué ocurre si λ=0 en Ridge o Lasso?**
Source: notas.md
- a. Se obtiene la regresión lineal clásica ✓
- b. Se eliminan todas las variables
- c. El modelo se vuelve no lineal

10. Qué riesgo aumenta al incrementar el grado del polinomio?**
Source: notas.md
- a. Sobreajuste ✓
- b. Falta de convergencia numérica
- c. Sesgo

11. Cuál es el objetivo principal de las SVM?**
Source: notas.md
- a. Maximizar el error de clasificación
- b. Buscar el hiperplano con mayor margen entre clases ✓
- c. Minimizar el número de características

12. Qué son los vectores de soporte en SVM?**
Source: notas.md
- a. Los puntos más alejados de la frontera de decisión
- b. Los puntos más cercanos a la frontera de decisión ✓
- c. Puntos seleccionados aleatoriamente

13. Qué significa γ (gamma) alto en SVM con kernel RBF?**
Source: notas.md
- a. Fronteras suaves (bajo sesgo)
- b. Fronteras onduladas, muy localizadas (alto riesgo de sobreajuste) ✓
- c. Mayor generalización

14. Cuál es la función de activación estándar en redes modernas?**
Source: notas.md
- a. Sigmoide
- b. Tanh
- c. ReLU ✓

15. Qué hace la retropropagación en una red neuronal?**
Source: notas.md
- a. Propaga datos hacia adelante
- b. Calcula gradientes de la función de pérdida para actualizar parámetros ✓
- c. Escala las variables de entrada

16. Para qué se utiliza Dropout en redes neuronales?**
Source: notas.md
- a. Para acelerar el entrenamiento
- b. Para reducir sobreajuste desactivando aleatoriamente neuronas ✓
- c. Para aumentar la precisión

17. Cuándo es mejor usar SVM sobre redes neuronales?**
Source: notas.md
- a. Siempre son superiores las redes neuronales
- b. Con datasets pequeños/medianos y cuando interpretabilidad es importante ✓
- c. SVM es siempre mejor

18. Qué algoritmo de optimización es alternativa al SGD clásico?**
Source: notas.md
- a. Newton-Raphson
- b. Backtracking
- c. Adam ✓

19. Qué kernel se relaciona conceptualmente con las neuronas artificiales?**
Source: notas.md
- a. Polinomial
- b. RBF
- c. Sigmoide ✓

20. Qué función de pérdida es común en clasificación con redes neuronales?**
Source: notas.md
- a. MSE
- b. Entropía cruzada ✓
- c. Log-loss

21. Qué mide la función f(x)=w?x+b en SVM?**
Source: notas.md
- a. La distancia al hiperplano ✓
- b. El número de vectores de soporte
- c. La probabilidad de clase

22. Qué kernel es más adecuado cuando los datos son linealmente separables?**
Source: notas.md
- a. Kernel RBF
- b. Kernel polinomial
- c. Kernel lineal ✓

23. Qué ocurre si se seleccionan hiperparámetros usando el conjunto de prueba?**
Source: notas.md
- a. Mejora generalización
- b. No tiene consecuencias
- c. Se produce fuga de información y evaluación optimista ✓

24. Qué salida produce una capa Softmax en redes neuronales?**
Source: notas.md
- a. Probabilidades normalizadas multiclase ✓
- b. Valores entre -1 y 1
- c. Distancias al hiperplano

25. Qué función de activación es estándar en redes modernas por su eficiencia?**
Source: notas.md
- a. Sigmoide
- b. Tanh
- c. ReLU ✓

26. Cuál es el rol de los vectores de soporte en SVM?**
Source: notas.md
- a. Son los puntos más cercanos al hiperplano que definen la frontera ✓
- b. Son los puntos más alejados del hiperplano
- c. Son todos los puntos de entrenamiento

27. Qué busca maximizar una SVM lineal al separar clases?**
Source: notas.md
- a. El margen entre las clases ✓
- b. El número de parámetros del modelo
- c. El número de vectores de soporte

28. Qué función de activación se usa típicamente en clasificación binaria por probabilidades?**
Source: notas.md
- a. ReLU
- b. Tanh
- c. Sigmoide ✓

29. Qué técnica ayuda a detener el entrenamiento antes del sobreajuste?**
Source: notas.md
- a. Expansión de dataset
- b. Early stopping ✓
- c. Regularización L1

30. Cuál es una diferencia práctica entre SVM y redes neuronales?**
Source: notas.md
- a. SVM requiere más datos
- b. SVM es más eficiente en datasets pequeños ✓
- c. RNA es más interpretable

31. Qué combina una neurona artificial antes de aplicar la función de activación?**
Source: notas.md
- a. Un producto cruzado entre entradas
- b. Una resta entre entradas
- c. Una suma ponderada más un sesgo ✓

32. Qué representa el hiperparámetro C en una SVM?**
Source: notas.md
- a. El número de vectores de soporte
- b. El grado de penalización por errores de entrenamiento ✓
- c. La tasa de aprendizaje del modelo

33. Qué efecto tiene un gamma (γ) alto en un kernel RBF?**
Source: notas.md
- a. Fronteras suaves y generalización amplia
- b. Fronteras muy onduladas y riesgo de sobreajuste ✓
- c. Disminución de la dimensionalidad

34. Qué rol tiene el sesgo (b) en una neurona?**
Source: notas.md
- a. Aumenta el número de neuronas
- b. Desplaza la función de activación ✓
- c. Evita la regularización

35. Qué problema clásico no puede resolver un perceptrón simple?**
Source: notas.md
- a. Problema XOR ✓
- b. Regresión lineal
- c. Clasificación lineal

36. Qué técnica evita sobreajuste en redes neuronales?**
Source: notas.md
- a. Usar siempre sigmoide
- b. Dropout ✓
- c. Aumentar neuronas sin límite

37. Qué representan los nodos internos en un árbol de decisión?
Source: notas.md
- a. ) Predicciones finales.
- b. ) Condiciones de partición sobre variables. () ✓
- c. ) Registros individuales de entrenamiento.
- d. orrecta: b) Condiciones de partición sobre variables.

38. Qué efecto tiene la poda en un árbol de decisión?
Source: notas.md
- a. ) Aumentar el número de nodos terminales.
- b. ) Calcular de nuevo la entropía.
- c. ) Reducir ramas innecesarias para mejorar generalización. () ✓
- d. orrecta: c) Reducir ramas innecesarias para mejorar generalización.

39. Qué sucede con la capacidad de generalización de un árbol muy profundo?
Source: notas.md
- a. ) Permanece igual.
- b. ) Se incrementa siempre.
- c. ) Se reduce al aprender ruido. () ✓
- d. orrecta: c) Se reduce al aprender ruido.

40. Cuál es el riesgo de no podar un árbol de decisión?
Source: notas.md
- a. ) Eliminación de nodos homogéneos.
- b. ) Reducción de sesgo.
- c. ) Captura de ruido en los datos. () ✓
- d. orrecta: c) Captura de ruido en los datos.

41. Qué tipo de pregunta representa cada nodo interno de un árbol de decisión?
Source: notas.md
- a. ) Una operación aritmética.
- b. ) Un promedio ponderado.
- c. ) Una condición sobre una variable. () ✓
- d. orrecta: c) Una condición sobre una variable.

42. Qué ocurre si un árbol es demasiado poco profundo?
Source: notas.md
- a. ) Se subajusta. () ✓
- b. ) Se sobreajusta.
- c. ) No genera predicciones.
- d. orrecta: a) Se subajusta.

43. Qué ocurre si se limita demasiado la profundidad de un árbol?
Source: notas.md
- a. ) Puede perder patrones relevantes. () ✓
- b. ) Mejora la generalización siempre.
- c. ) La entropía se anula.
- d. orrecta: a) Puede perder patrones relevantes.

44. Qué criterio es computacionalmente más eficiente en la práctica?
Source: notas.md
- a. ) El índice de Gini. () ✓
- b. ) La entropía.
- c. ) El promedio de clases.
- d. orrecta: a) El índice de Gini.

45. Qué relación tienen los árboles de decisión con el sesgo y la varianza?
Source: notas.md
- a. ) Siempre tienen alto sesgo.
- b. ) Pueden regularse para equilibrar ambos. () ✓
- c. ) Siempre tienen baja varianza.
- d. orrecta: b) Pueden regularse para equilibrar ambos.

46. Qué representa un valor de Gini cercano a 0.5 en un nodo binario?
Source: notas.md
- a. ) Un nodo eliminado por poda.
- b. ) Un nodo muy mezclado. () ✓
- c. ) Un nodo puro.
- d. orrecta: b) Un nodo muy mezclado.

47. Qué significa que la entropía sea igual a 0 en un nodo?
Source: notas.md
- a. ) El nodo contiene solo ejemplos positivos.
- b. ) El nodo es completamente puro. () ✓
- c. ) El nodo tiene incertidumbre máxima.
- d. orrecta: b) El nodo es completamente puro.

48. Qué implica que un árbol tenga baja profundidad y alto error en entrenamiento?
Source: notas.md
- a. ) Está sobreajustado.
- b. ) Está subajustado. () ✓
- c. ) Tiene baja varianza.
- d. orrecta: b) Está subajustado.

49. Qué estrategia permite regular la complejidad de un árbol antes de crecer completamente?
Source: notas.md
- a. ) Cálculo del error cuadrático medio.
- b. ) Ajuste de hiperparámetros. () ✓
- c. ) Aumento de hojas terminales.
- d. orrecta: b) Ajuste de hiperparámetros.

50. Qué refleja el dilema entre sesgo y varianza en árboles de decisión?
Source: notas.md
- a. ) El método de optimización.
- b. ) El equilibrio entre simplicidad y capacidad de generalización. () ✓
- c. ) El número de variables predictoras.
- d. orrecta: b) El equilibrio entre simplicidad y capacidad de generalización.

51. Qué mide la entropía en un árbol de decisión?
Source: notas.md
- a. ) La cantidad de nodos.
- b. ) El número de divisiones realizadas.
- c. ) El nivel de incertidumbre de la distribución de clases. () ✓
- d. orrecta: c) El nivel de incertidumbre de la distribución de clases.

52. Qué significa que el índice de Gini sea cercano a 0?
Source: notas.md
- a. ) La partición es heterogénea.
- b. ) La partición es homogénea. () ✓
- c. ) El árbol está sobreajustado.
- d. orrecta: b) La partición es homogénea.

53. Qué tipo de pregunta representa cada nodo interno de un árbol de decisión?
Source: notas.md
- a. ) Una condición sobre una variable. () ✓
- b. ) Una operación aritmética.
- c. ) Un promedio ponderado.
- d. orrecta: a) Una condición sobre una variable.

54. Cuál es el riesgo de no podar un árbol de decisión?
Source: notas.md
- a. ) Eliminación de nodos homogéneos.
- b. ) Captura de ruido en los datos. () ✓
- c. ) Reducción de sesgo.
- d. orrecta: b) Captura de ruido en los datos.

55. Qué puede suceder si se permite que los nodos de un árbol se dividan con muy pocas muestras?
Source: notas.md
- a. ) El árbol se vuelve demasiado complejo y tiende a sobreajustar. () ✓
- b. ) El modelo aumenta su sesgo de manera significativa.
- c. ) El árbol se vuelve más general y sencillo.
- d. orrecta: a) El árbol se vuelve demasiado complejo y tiende a sobreajustar.

56. Qué criterio es computacionalmente más eficiente en la práctica?
Source: notas.md
- a. ) El índice de Gini. () ✓
- b. ) El promedio de clases.
- c. ) La entropía.
- d. orrecta: a) El índice de Gini.

57. Por qué la exactitud es engañosa en detección de fraudes?
Source: notas.md
- a. ) Porque la clase fraudulenta es mayoritaria.
- b. ) Porque no mide la precisión en tiempo real.
- c. ) Porque un modelo puede predecir siempre "no fraude" y tener alta accuracy. () ✓
- d. orrecta: c) Porque un modelo puede predecir siempre "no fraude" y tener alta accuracy.

58. Qué visión fomenta el análisis de errores en estudiantes?
Source: notas.md
- a. ) Que solo importa el F1-score.
- b. ) Una mirada crítica para evaluar limitaciones y mejoras. () ✓
- c. ) Que los modelos son siempre exactos.
- d. orrecta: b) Una mirada crítica para evaluar limitaciones y mejoras.

59. Por qué se prioriza el recall en problemas médicos?
Source: notas.md
- a. ) Porque es más grave no detectar un caso positivo que detectarlo erróneamente. () ✓
- b. ) Porque siempre da valores más altos que la precisión.
- c. ) Porque se busca minimizar la cantidad de predicciones negativas.
- d. orrecta: a) Porque es más grave no detectar un caso positivo que detectarlo erróneamente.

60. Qué representa un falso negativo en un dataset de salud?
Source: notas.md
- a. ) Diagnosticar correctamente la ausencia de enfermedad.
- b. ) Detectar erróneamente enfermedad en un paciente sano.
- c. ) No detectar enfermedad en un paciente que sí la tiene. () ✓
- d. orrecta: c) No detectar enfermedad en un paciente que sí la tiene.

61. Qué mide el recall (sensibilidad) para una clase?
Source: notas.md
- a. ) La proporción de falsos positivos sobre el total de predicciones positivas.
- b. ) La proporción de verdaderos positivos sobre todos los casos realmente positivos. () ✓
- c. ) La proporción de predicciones correctas sobre el total de predicciones.
- d. orrecta: b) La proporción de verdaderos positivos sobre todos los casos realmente positivos.

62. Por qué la accuracy puede ser engañosa en un problema multiclase desbalanceado?
Source: notas.md
- a. ) Porque un modelo puede acertar mayormente en clases frecuentes y fallar en las minoritarias. () ✓
- b. ) Porque siempre da un valor bajo en cualquier escenario.
- c. ) Porque solo mide los errores en la clase mayoritaria.
- d. orrecta: a) Porque un modelo puede acertar mayormente en clases frecuentes y fallar en las minoritarias.

63. Qué enseñan los errores en modelos de aprendizaje automático?
Source: notas.md
- a. ) Que los errores pueden ser pistas para mejorar modelos y datos. () ✓
- b. ) Que los algoritmos son siempre incorrectos.
- c. ) Que las métricas no son necesarias.
- d. orrecta: a) Que los errores pueden ser pistas para mejorar modelos y datos.

64. Qué indica un patrón sistemático en los errores?
Source: notas.md
- a. ) Posible sesgo en los datos o el modelo. () ✓
- b. ) Varianza alta.
- c. ) Aleatoriedad total en los errores.
- d. orrecta: a) Posible sesgo en los datos o el modelo.

65. Qué son los falsos positivos (FP) en clasificación?
Source: notas.md
- a. ) Casos correctamente clasificados en la clase positiva.
- b. ) Casos predichos como negativos siendo positivos.
- c. ) Casos predichos como positivos siendo negativos. () ✓
- d. orrecta: c) Casos predichos como positivos siendo negativos.

66. Cómo puede mejorar un modelo con sesgo hacia precios bajos?
Source: notas.md
- a. ) Eliminando la mitad de los datos.
- b. ) Usando técnicas de regularización o nuevas variables. () ✓
- c. ) Incrementando aleatoriamente los precios reales.
- d. orrecta: b) Usando técnicas de regularización o nuevas variables.

67. Por qué la exactitud es engañosa en detección de fraudes?
Source: notas.md
- a. ) Porque la clase fraudulenta es mayoritaria.
- b. ) Porque no mide la precisión en tiempo real.
- c. ) Porque un modelo puede predecir siempre "no fraude" y tener alta accuracy. () ✓
- d. orrecta: c) Porque un modelo puede predecir siempre "no fraude" y tener alta accuracy.

68. Qué muestra un gráfico de residuos en regresión?
Source: notas.md
- a. ) La tasa de falsos positivos y negativos.
- b. ) La distribución de las clases por categoría.
- c. ) La diferencia entre valores predichos y observados. () ✓
- d. orrecta: c) La diferencia entre valores predichos y observados.

69. Qué enseñan los errores en modelos de aprendizaje automático?
Source: notas.md
- a. ) Que las métricas no son necesarias.
- b. ) Que los errores pueden ser pistas para mejorar modelos y datos. () ✓
- c. ) Que los algoritmos son siempre incorrectos.
- d. orrecta: b) Que los errores pueden ser pistas para mejorar modelos y datos.

70. Qué tipo de datasets suelen presentar ruido y valores faltantes?
Source: notas.md
- a. ) Datasets sintéticos.
- b. ) Datasets balanceados.
- c. ) Datasets reales. () ✓
- d. orrecta: c) Datasets reales.

71. Qué rol tiene el análisis de residuos en predicción de precios de vivienda?
Source: notas.md
- a. ) Ajustar automáticamente los hiperparámetros.
- b. ) Ver la distribución de las etiquetas reales.
- c. ) Identificar si el modelo subestima precios altos. () ✓
- d. orrecta: c) Identificar si el modelo subestima precios altos.

72. Qué son los falsos positivos (FP) en clasificación?
Source: notas.md
- a. ) Casos correctamente clasificados en la clase positiva.
- b. ) Casos predichos como positivos siendo negativos. () ✓
- c. ) Casos predichos como negativos siendo positivos.
- d. orrecta: b) Casos predichos como positivos siendo negativos.

73. Qué visión fomenta el análisis de errores en estudiantes?
Source: notas.md
- a. ) Que los modelos son siempre exactos.
- b. ) Una mirada crítica para evaluar limitaciones y mejoras. () ✓
- c. ) Que solo importa el F1-score.
- d. orrecta: b) Una mirada crítica para evaluar limitaciones y mejoras.

74. Qué penaliza el log-loss en clasificación?
Source: notas.md
- a. ) Los errores de predicción con baja probabilidad.
- b. ) Las predicciones incorrectas con alta confianza. () ✓
- c. ) Los aciertos en clases mayoritarias.
- d. orrecta: b) Las predicciones incorrectas con alta confianza.

75. Cómo puede extenderse el ROC-AUC a problemas multiclase?
Source: notas.md
- a. ) Usando el enfoque "uno contra todos" para cada clase. () ✓
- b. ) Calculando un valor único de exactitud.
- c. ) Promediando las matrices de confusión.
- d. orrecta: a) Usando el enfoque "uno contra todos" para cada clase.

76. Cómo funciona el weighted average en clasificación multiclase?
Source: notas.md
- a. ) Usa el promedio de métricas más altas.
- b. ) Ignora las clases con baja frecuencia.
- c. ) Pondera cada clase según su proporción en el dataset. () ✓
- d. orrecta: c) Pondera cada clase según su proporción en el dataset.

77. Cómo puede mejorar un modelo con sesgo hacia precios bajos?
Source: notas.md
- a. ) Usando técnicas de regularización o nuevas variables. () ✓
- b. ) Incrementando aleatoriamente los precios reales.
- c. ) Eliminando la mitad de los datos.
- d. orrecta: a) Usando técnicas de regularización o nuevas variables.

78. Por qué se prioriza el recall en problemas médicos?
Source: notas.md
- a. ) Porque se busca minimizar la cantidad de predicciones negativas.
- b. ) Porque siempre da valores más altos que la precisión.
- c. ) Porque es más grave no detectar un caso positivo que detectarlo erróneamente. () ✓
- d. orrecta: c) Porque es más grave no detectar un caso positivo que detectarlo erróneamente.

79. Cuál es la fórmula del F1-score?
Source: notas.md
- a. ) F1=(Precisión+Recall)/2
- b. ) F1=(Precisión-Recall)/(Precisión+Recall)
- c. ) F1=2*(Precisión*Recall)/(Precisión+Recall) () ✓
- d. orrecta: c) F1=2*(Precisión*Recall)/(Precisión+Recall).

80. Qué son los falsos negativos (FN)?
Source: notas.md
- a. ) Casos predichos como positivos siendo positivos.
- b. ) Casos correctamente clasificados como negativos.
- c. ) Casos predichos como negativos siendo positivos. () ✓
- d. orrecta: c) Casos predichos como negativos siendo positivos.

81. Qué refleja el análisis de palabras mal clasificadas en spam?
Source: notas.md
- a. ) Que algunos patrones lingüísticos inducen a error al modelo. () ✓
- b. ) Que el modelo tiene varianza infinita.
- c. ) Que el dataset no sirve.
- d. orrecta: a) Que algunos patrones lingüísticos inducen a error al modelo.

82. Qué indica un patrón sistemático en los errores?
Source: notas.md
- a. ) Varianza alta.
- b. ) Posible sesgo en los datos o el modelo. () ✓
- c. ) Aleatoriedad total en los errores.
- d. orrecta: b) Posible sesgo en los datos o el modelo.

83. Qué problema se observa en la detección de spam?
Source: notas.md
- a. ) El desbalance entre spam y no spam. () ✓
- b. ) El log-loss siempre es bajo.
- c. ) Los correos legítimos siempre se clasifican como spam.
- d. orrecta: a) El desbalance entre spam y no spam.

84. Qué mide el índice Kappa de Cohen en clasificación?
Source: notas.md
- a. ) El porcentaje de falsos positivos.
- b. ) El tiempo de entrenamiento del modelo.
- c. ) El grado de acuerdo entre predicciones y realidad corrigiendo por azar. () ✓
- d. orrecta: c) El grado de acuerdo entre predicciones y realidad corrigiendo por azar.

85. Qué mide el recall (sensibilidad) para una clase?
Source: notas.md
- a. ) La proporción de falsos positivos sobre el total de predicciones positivas.
- b. ) La proporción de verdaderos positivos sobre todos los casos realmente positivos. () ✓
- c. ) La proporción de predicciones correctas sobre el total de predicciones.
- d. orrecta: b) La proporción de verdaderos positivos sobre todos los casos realmente positivos.

86. Qué significa la calidad de datos en ML?**
Source: notas.md
- a. Que ruido y valores faltantes afectan la validez del modelo. ✓
- b. Que los modelos pueden aprender incluso sin datos.
- c. Que basta con tener grandes volúmenes sin importar su fiabilidad.

87. Qué implica la complejidad computacional?**
Source: notas.md
- a. Que los modelos no requieren energía.
- b. Que solo funcionan en computadores personales antiguos.
- c. Que los modelos profundos necesitan hardware especializado y alto consumo. ✓

88. Qué tipo de ML se usa para entrenar un robot a caminar?**
Source: notas.md
- a. Auto-supervisado.
- b. Por refuerzo. ✓
- c. Semi-supervisado.

89. Cuál es la esencia del aprendizaje automático?**
Source: notas.md
- a. Memorizar todos los ejemplos de entrenamiento.
- b. Requerir supervisión humana en cada decisión.
- c. Generalizar a partir de ejemplos para predecir nuevos casos. ✓

90. Cuál es una aplicación en salud?**
Source: notas.md
- a. Diagnóstico asistido por imágenes médicas. ✓
- b. Monitoreo de redes sociales.
- c. Predicción de ventas minoristas.

91. Cuál fue un hito en IA en los 2010s?**
Source: notas.md
- a. El uso de reglas lógicas en todo sistema.
- b. El éxito de redes profundas en visión y lenguaje. ✓
- c. La exclusión de datos no estructurados.

92. En qué consiste el aprendizaje no supervisado?**
Source: notas.md
- a. Identifica estructuras ocultas en datos sin etiquetas. ✓
- b. No requiere procesamiento computacional.
- c. Depende de etiquetas predefinidas.

93. Cuál es una limitación ética central?**
Source: notas.md
- a. La reproducción de discriminaciones sociales. ✓
- b. La precisión excesiva.
- c. El consumo eléctrico de GPUs.

94. Qué distingue al aprendizaje supervisado?**
Source: notas.md
- a. Utiliza conjuntos de datos con etiquetas conocidas. ✓
- b. Siempre requiere que los datos no tengan etiquetas.
- c. Se centra únicamente en simular redes neuronales.

95. Por qué es importante la interpretabilidad?**
Source: notas.md
- a. Porque mejora la velocidad de cómputo.
- b. Porque sustituye la necesidad de pruebas estadísticas.
- c. Porque en áreas críticas se requiere explicar decisiones. ✓

96. Cuál fue un hito en IA en los 2010s?**
Source: notas.md
- a. El éxito de redes profundas en visión y lenguaje. ✓
- b. El uso de reglas lógicas en todo sistema.
- c. La exclusión de datos no estructurados.

97. Qué problema busca resolver el aprendizaje auto-supervisado en NLP?**
Source: notas.md
- a. Mejorar hardware de GPUs.
- b. Reducir costos en satélites.
- c. Crear representaciones de lenguaje sin etiquetas manuales. ✓

98. En qué década surgió el término "inteligencia artificial"?**
Source: notas.md
- a. 1940.
- b. 1980.
- c. 1950. ✓

99. Qué permitió el resurgimiento de la IA en los 2000?**
Source: notas.md
- a. Mayor poder computacional y big data. ✓
- b. La desaparición de la estadística.
- c. La caída de internet.

100. Por qué es clave la transparencia en medicina?**
Source: notas.md
- a. Para aumentar la velocidad de consultas.
- b. Para reducir el costo de tratamientos.
- c. Para que médicos y pacientes comprendan las decisiones del modelo. ✓

101. Qué distingue al aprendizaje supervisado?**
Source: notas.md
- a. Siempre requiere que los datos no tengan etiquetas.
- b. Se centra únicamente en simular redes neuronales.
- c. Utiliza conjuntos de datos con etiquetas conocidas. ✓

102. Qué hace único al aprendizaje auto-supervisado?**
Source: notas.md
- a. Genera etiquetas artificiales a partir de los propios datos. ✓
- b. Depende exclusivamente de hardware especializado.
- c. No utiliza datos.

103. En qué consiste el aprendizaje no supervisado?**
Source: notas.md
- a. Depende de etiquetas predefinidas.
- b. No requiere procesamiento computacional.
- c. Identifica estructuras ocultas en datos sin etiquetas. ✓

104. Qué tipo de ML se usa para entrenar un robot a caminar?**
Source: notas.md
- a. Semi-supervisado.
- b. Auto-supervisado.
- c. Por refuerzo. ✓

105. Qué significa la calidad de datos en ML?**
Source: notas.md
- a. Que ruido y valores faltantes afectan la validez del modelo. ✓
- b. Que basta con tener grandes volúmenes sin importar su fiabilidad.
- c. Que los modelos pueden aprender incluso sin datos.

106. Cuál es un desafío clave en la implementación de ML en educación?**
Source: notas.md
- a. Que los modelos siempre generan mejores profesores.
- b. Que no requieren datos de estudiantes.
- c. Evitar sesgos en recomendaciones personalizadas. ✓

107. Qué implica la complejidad computacional?**
Source: notas.md
- a. Que los modelos no requieren energía.
- b. Que los modelos profundos necesitan hardware especializado y alto consumo. ✓
- c. Que solo funcionan en computadores personales antiguos.

108. Qué representa la figura del espectro de aplicaciones de IA?**
Source: notas.md
- a. Que cubre desde asistencia humana hasta automatización completa. ✓
- b. Que se restringe a educación y salud.
- c. Que solo sirve en entornos militares.

109. Cuál es la característica del aprendizaje semi-supervisado?**
Source: notas.md
- a. Solo funciona con datos completamente etiquetados.
- b. Combina datos etiquetados y no etiquetados. ✓
- c. Se limita a tareas de predicción de precios.

110. Qué busca la IA explicable (XAI)?**
Source: notas.md
- a. Reducir el costo del hardware.
- b. Aumentar la velocidad de procesamiento.
- c. Transparencia en las decisiones de los modelos. ✓

111. Qué papel cumple el álgebra lineal en el aprendizaje automático?**
Source: notas.md
- a. Define reglas de lógica simbólica.
- b. Facilita la edición de imágenes en alta resolución.
- c. Permite representar datos en vectores y matrices y aplicar transformaciones lineales. ✓

112. Qué ventaja principal ofrecen los Jupyter Notebooks?**
Source: notas.md
- a. Reemplazan los sistemas operativos tradicionales.
- b. Permiten crear animaciones 3D automáticamente.
- c. Integran código, texto y visualizaciones en un solo documento. ✓

113. Cómo se representan normalmente los datos en álgebra lineal dentro del aprendizaje automático?**
Source: notas.md
- a. Como tablas periódicas.
- b. Como ecuaciones diferenciales.
- c. Como vectores y matrices. ✓

114. Qué caracteriza al aprendizaje supervisado?**
Source: notas.md
- a. Se entrena con pares entrada-salida. ✓
- b. No requiere etiquetas.
- c. Solo se usa en clustering.

115. Qué biblioteca es clave en Python para manipulación de arreglos numéricos?**
Source: notas.md
- a. NumPy. ✓
- b. BeautifulSoup.
- c. Seaborn.

116. Qué caracteriza al aprendizaje no supervisado?**
Source: notas.md
- a. El modelo encuentra patrones sin etiquetas previas. ✓
- b. Solo se usa en imágenes médicas.
- c. Los datos incluyen etiquetas definidas.

117. Qué lenguaje domina el ecosistema de ML?**
Source: notas.md
- a. Python. ✓
- b. C puro.
- c. Java.

118. Qué ventaja tiene usar Google Colab sobre otros entornos?**
Source: notas.md
- a. No permite compartir proyectos.
- b. Carece de acceso a bibliotecas de Python.
- c. Ofrece recursos gratuitos en la nube para ejecutar modelos. ✓

119. Qué aportan las estadísticas al aprendizaje automático?**
Source: notas.md
- a. Ofrecen métodos de inferencia y validación para asegurar la generalización. ✓
- b. Permiten únicamente calcular promedios.
- c. Ayudan a diseñar arquitecturas neuronales profundas.

120. Qué caracteriza al aprendizaje no supervisado?**
Source: notas.md
- a. Descubre estructuras ocultas sin etiquetas. ✓
- b. Depende exclusivamente de pruebas de hipótesis.
- c. Utiliza regresión lineal.

121. Qué relación tiene la probabilidad con los modelos de Markov?**
Source: notas.md
- a. Solo sirven en álgebra lineal.
- b. Modelan procesos estocásticos y secuenciales. ✓
- c. Representan datos deterministas.

122. Cómo se representan normalmente los datos en álgebra lineal dentro del aprendizaje automático?**
Source: notas.md
- a. Como tablas periódicas.
- b. Como ecuaciones diferenciales.
- c. Como vectores y matrices. ✓

123. Qué caracteriza al aprendizaje supervisado?**
Source: notas.md
- a. No requiere etiquetas.
- b. Solo se usa en clustering.
- c. Se entrena con pares entrada-salida. ✓

124. Por qué la integración de álgebra lineal, probabilidad y estadística es esencial en ML?**
Source: notas.md
- a. Porque son asignaturas independientes.
- b. Porque eliminan la necesidad de programación.
- c. Porque juntas permiten diseñar algoritmos robustos y generalizables. ✓

125. Qué caracteriza al aprendizaje semi-supervisado?**
Source: notas.md
- a. Usa solo datos etiquetados.
- b. Combina datos etiquetados y no etiquetados. ✓
- c. Requiere árboles de decisión siempre.

126. Qué caracteriza al aprendizaje no supervisado?**
Source: notas.md
- a. Los datos incluyen etiquetas definidas.
- b. Solo se usa en imágenes médicas.
- c. El modelo encuentra patrones sin etiquetas previas. ✓

127. Qué caracteriza al aprendizaje no supervisado?**
Source: notas.md
- a. Utiliza regresión lineal.
- b. Descubre estructuras ocultas sin etiquetas. ✓
- c. Depende exclusivamente de pruebas de hipótesis.

128. Qué aportan las estadísticas al aprendizaje automático?**
Source: notas.md
- a. Ayudan a diseñar arquitecturas neuronales profundas.
- b. Permiten únicamente calcular promedios.
- c. Ofrecen métodos de inferencia y validación para asegurar la generalización. ✓

129. Qué entorno interactivo permite documentar procesos reproducibles?**
Source: notas.md
- a. Jupyter Notebook. ✓
- b. Visual Studio Code.
- c. Eclipse.

130. Cuál es la función de pandas?**
Source: notas.md
- a. Manipular y analizar datos en tablas (DataFrames). ✓
- b. Renderizar gráficos 3D.
- c. Crear redes neuronales profundas.

131. Qué biblioteca es clave en Python para manipulación de arreglos numéricos?**
Source: notas.md
- a. BeautifulSoup.
- b. NumPy. ✓
- c. Seaborn.

132. Qué lenguaje domina el ecosistema de ML?**
Source: notas.md
- a. Java.
- b. Python. ✓
- c. C puro.

133. Por qué la estadística es fundamental en validación de modelos?**
Source: notas.md
- a. Para graficar redes neuronales.
- b. Para construir arquitecturas convolucionales.
- c. Para aplicar pruebas de hipótesis y asegurar generalización. ✓

134. Qué biblioteca se usa para visualización en ML?**
Source: notas.md
- a. Keras.
- b. TensorFlow.
- c. Matplotlib. ✓

135. Qué papel cumple el álgebra lineal en el aprendizaje automático?**
Source: notas.md
- a. Define reglas de lógica simbólica.
- b. Permite representar datos en vectores y matrices y aplicar transformaciones lineales. ✓
- c. Facilita la edición de imágenes en alta resolución.

136. Qué ventaja tiene usar Google Colab sobre otros entornos?**
Source: notas.md
- a. Carece de acceso a bibliotecas de Python.
- b. No permite compartir proyectos.
- c. Ofrece recursos gratuitos en la nube para ejecutar modelos. ✓

137. Qué es MLOps?**
Source: notas.md
- a. Prácticas que integran ingeniería de software y ciencia de datos para producción. ✓
- b. Un tipo de regresión lineal.
- c. Un algoritmo de clustering jerárquico.

138. Qué significa un modelo con accuracy = 0.95 en dataset muy desbalanceado (95% negativos)?**
Source: notas.md
- a. Puede estar ignorando casi todos los positivos ✓
- b. Clasifica bien ambas clases
- c. Tiene recall perfecto

139. Qué métrica es más adecuada cuando los falsos positivos son muy costosos?**
Source: notas.md
- a. R²
- b. Precision ✓
- c. Recall

140. Cuál es el propósito principal de la trazabilidad en el ciclo de vida de un modelo de ML?**
Source: notas.md
- a. Aumentar la velocidad de entrenamiento
- b. Documentar y verificar decisiones y riesgos ✓
- c. Reducir el tamaño del dataset

141. Qué función se relaciona con mapear riesgos y supuestos en el diseño?**
Source: notas.md
- a. MANAGE
- b. MEASURE
- c. MAP ✓

142. Qué ocurre con el recall si aumentan los falsos negativos?**
Source: notas.md
- a. Se mantiene igual
- b. Aumenta
- c. Disminuye ✓

143. Qué combinación refleja un modelo con alta precisión pero bajo recall?**
Source: notas.md
- a. Muchos FN y pocos FP ✓
- b. Muchos FP y pocos FN
- c. Pocos FN y muchos FP

144. Cuál es el propósito principal de dividir los datos en entrenamiento, validación y prueba?**
Source: notas.md
- a. Para acelerar el entrenamiento de los modelos
- b. Para evaluar generalización de manera confiable ✓
- c. Para evitar el uso de algoritmos complejos

145. Qué es validación cruzada anidada?**
Source: notas.md
- a. Una variante de K-fold con menos pliegues
- b. Un bucle interno para hiperparámetros y externo para evaluación ✓
- c. Entrenar con menos datos para ahorrar tiempo

146. Qué refleja el término "fuga de información"?**
Source: notas.md
- a. Baja precisión por desbalance
- b. Uso indebido de datos de validación o futuro en entrenamiento ✓
- c. Pérdida de datos durante el entrenamiento

147. Qué sucede si el error de entrenamiento es muy bajo pero validación sigue alto?**
Source: notas.md
- a. Subajuste
- b. Sobreajuste ✓
- c. Modelo balanceado

148. Qué parámetro se ajustó en el video para evitar que el árbol se sobreajuste?**
Source: notas.md
- a. Learning rate
- b. Máxima profundidad del árbol ✓
- c. Número de pliegues

149. Qué métrica NO es adecuada en un dataset desbalanceado?**
Source: notas.md
- a. Accuracy ✓
- b. F1-score
- c. Recall

150. Cuál de los siguientes síntomas refleja sobreajuste?**
Source: notas.md
- a. Ambos errores altos
- b. Error bajo en entrenamiento pero alto en validación ✓
- c. Error alto en entrenamiento y validación

151. Qué caracteriza a la validación cruzada K-fold?**
Source: notas.md
- a. Usa siempre el mismo corte de datos
- b. Divide en K pliegues y rota validación ✓
- c. Entrena con todo y valida con todo

152. Qué sucede cuando se aplica dropout en una red neuronal?**
Source: notas.md
- a. Se desactivan aleatoriamente durante entrenamiento ✓
- b. Se eliminan definitivamente neuronas
- c. Se reducen los datos de entrada
