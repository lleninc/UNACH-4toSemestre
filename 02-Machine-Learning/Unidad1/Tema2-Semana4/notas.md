# 02-Machine-Learning - U1 T2 S4

## Notas de clase

### 2. Tema 2: Principios de modelado y validación

Esta semana se enfoca en dos ideas críticas para juzgar si un modelo de ML es confiable: cómo dividir correctamente los datos y cómo detectar si el modelo está aprendiendo demasiado o demasiado poco.

### 2.3 Validación cruzada y división de datos

Dividir los datos correctamente evita una de las fallas más comunes en ML: creer que un modelo funciona bien cuando en realidad solo memorizó los ejemplos vistos.

#### División básica de datos

La forma más simple de separar el conjunto de datos es dividirlo en tres partes:

- **Entrenamiento:** para aprender patrones.
- **Validación:** para ajustar hiperparámetros y comparar modelos.
- **Prueba:** para estimar el rendimiento final.

#### Proporciones comunes

| División | Uso | Ejemplo típico |
|---------|-----|----------------|
| 70/15/15 | entrenamiento / validación / prueba | Proyectos académicos y prototipos |
| 80/20 | entrenamiento / prueba | Casos simples o conjuntos pequeños |
| 60/20/20 | entrenamiento / validación / prueba | Cuando se quiere una validación más clara |

**Regla importante:** el conjunto de prueba no debe usarse para ajustar el modelo. Solo se consulta al final.

#### Validación cruzada

La validación cruzada evalúa un modelo varias veces usando diferentes particiones del conjunto de datos.

La versión más usada es la **k-fold cross-validation**:

1. Se divide el conjunto en $k$ partes.
2. Se entrena el modelo en $k-1$ partes.
3. Se valida en la parte restante.
4. Se repite el proceso $k$ veces.
5. Se promedian los resultados.

#### Ventajas de la validación cruzada

- Usa mejor los datos disponibles.
- Da una estimación más estable del desempeño.
- Reduce el riesgo de depender de una sola división afortunada o desafortunada.

#### Desventajas

- Requiere más tiempo de cómputo.
- Puede ser costosa con modelos complejos o datos muy grandes.

#### Idea clave sobre la división de datos

| Tipo de conjunto | Pregunta que responde | Se usa para |
|------------------|-----------------------|-------------|
| Entrenamiento | ¿Qué aprende el modelo? | Ajustar parámetros del modelo |
| Validación | ¿Qué versión del modelo funciona mejor? | Afinar hiperparámetros |
| Prueba | ¿Cómo funcionaría en datos nuevos? | Medir desempeño final |

### 2.4 Sobreajuste y subajuste

Estos dos problemas explican por qué un modelo puede verse excelente en entrenamiento pero fallar en la práctica.

#### Sobreajuste (overfitting)

Ocurre cuando el modelo aprende demasiado bien los datos de entrenamiento, incluyendo ruido y detalles irrelevantes.

**Síntoma típico:** rendimiento muy alto en entrenamiento y bajo en validación o prueba.

**Causa frecuente:** modelo demasiado complejo para la cantidad de datos disponible.

**Ejemplo:** memorizar respuestas en lugar de comprender el patrón.

#### Subajuste (underfitting)

Ocurre cuando el modelo es demasiado simple o no aprende lo suficiente de los datos.

**Síntoma típico:** rendimiento bajo tanto en entrenamiento como en validación.

**Causa frecuente:** modelo insuficiente, pocas variables, entrenamiento corto o mala representación de los datos.

#### Comparación rápida

| Situación | Error en entrenamiento | Error en validación | Interpretación |
|----------|------------------------|---------------------|----------------|
| Buen ajuste | Bajo | Bajo | El modelo generaliza bien |
| Sobreajuste | Muy bajo | Alto | Memoriza datos, no generaliza |
| Subajuste | Alto | Alto | El modelo no aprende suficiente |

#### Cómo reducir el sobreajuste

- Obtener más datos.
- Simplificar el modelo.
- Usar regularización.
- Aplicar validación cruzada.
- Seleccionar características relevantes.
- Detener el entrenamiento a tiempo.

#### Cómo reducir el subajuste

- Usar un modelo más expresivo.
- Agregar variables o características útiles.
- Entrenar por más tiempo.
- Reducir restricciones excesivas.
- Mejorar el preprocesamiento de datos.

#### Relación con el sesgo y la varianza

- **Sesgo alto:** suele asociarse con subajuste.
- **Varianza alta:** suele asociarse con sobreajuste.

El objetivo es encontrar un equilibrio entre ambos.

### Resumen conceptual

- Dividir mal los datos produce evaluaciones engañosas.
- La validación cruzada da una estimación más robusta.
- Sobreajuste significa aprender demasiado del entrenamiento.
- Subajuste significa aprender demasiado poco.
- Un buen modelo logra equilibrio entre complejidad y generalización.

## Quiz

### Pregunta 1: Uso del conjunto de prueba

**Pregunta:** ¿Para qué debe usarse el conjunto de prueba?

**Opciones:**
- ❌ Para ajustar hiperparámetros.
- ✅ **Para medir el desempeño final del modelo.**
- ❌ Para entrenar el modelo varias veces.

**Por qué:** el conjunto de prueba debe permanecer separado para estimar cómo responderá el modelo a datos nuevos.

### Pregunta 2: Validación cruzada

**Pregunta:** ¿Cuál es la idea principal de la validación cruzada?

**Opciones:**
- ✅ **Evaluar el modelo varias veces con distintas particiones de los datos.**
- ❌ Usar solo el conjunto de prueba en cada iteración.
- ❌ Entrenar con datos ya etiquetados manualmente por el profesor.

**Por qué:** la validación cruzada promedia varios resultados para obtener una evaluación más confiable.

### Pregunta 3: Sobreajuste

**Pregunta:** ¿Qué describe mejor el sobreajuste?

**Opciones:**
- ✅ **El modelo aprende incluso el ruido de los datos de entrenamiento.**
- ❌ El modelo no logra aprender ni siquiera patrones básicos.
- ❌ El modelo solo funciona con datos numéricos.

**Por qué:** sobreajustar es memorizar en vez de generalizar.

### Pregunta 4: Subajuste

**Pregunta:** ¿Qué ocurre en el subajuste?

**Opciones:**
- ❌ El modelo tiene desempeño alto en entrenamiento y bajo en prueba.
- ✅ **El modelo falla en entrenamiento y también en validación.**
- ❌ El modelo solo se usa en clustering.

**Por qué:** un modelo subajustado es demasiado simple o insuficiente para capturar la estructura de los datos.

### Pregunta 5: Señal de sobreajuste

**Pregunta:** ¿Cuál es una señal típica de sobreajuste?

**Opciones:**
- ✅ **Muy buen desempeño en entrenamiento y mal desempeño en validación.**
- ❌ Mal desempeño en entrenamiento y validación por igual.
- ❌ Que el modelo use validación cruzada.

**Por qué:** si el entrenamiento sale excelente pero la validación cae, el modelo no está generalizando.

### Pregunta 6: Cómo reducir sobreajuste

**Pregunta:** ¿Qué acción ayuda a reducir el sobreajuste?

**Opciones:**
- ✅ **Simplificar el modelo o usar regularización.**
- ❌ Eliminar la evaluación.
- ❌ Mezclar entrenamiento y prueba.

**Por qué:** reducir complejidad o penalizar ajustes excesivos ayuda a generalizar mejor.

### Pregunta 7: Relación sesgo-varianza

**Pregunta:** ¿Con qué se asocia normalmente el subajuste?

**Opciones:**
- ✅ **Con sesgo alto.**
- ❌ Con varianza alta solamente.
- ❌ Con un conjunto de prueba muy grande.

**Por qué:** el subajuste aparece cuando el modelo es demasiado rígido o simple.

### Preguntas extraídas de los quizzes de la carpeta Quiz (con respuestas)

1. **¿Cuál es el propósito principal de dividir los datos en entrenamiento, validación y prueba?**
   - a. Para acelerar el entrenamiento de los modelos
   - b. Para evaluar generalización de manera confiable ✓
   - c. Para evitar el uso de algoritmos complejos

2. **En problemas de salud, ¿qué métrica suele priorizarse para minimizar falsos negativos?**
   - a. RMSE
   - b. Precisión (precision)
   - c. Recall (sensibilidad) ✓

3. **En validación cruzada K=5 con 1000 ejemplos, ¿cuántos se usan como validación en cada pliegue?**
   - a. 100
   - b. 200 ✓
   - c. 500

4. **Un dataset tiene 2000 registros. Con división 80/20 (entrenamiento/prueba), ¿cuántos van a prueba?**
   - a. 1600
   - b. 400 ✓
   - c. 200

5. **¿Qué es validación cruzada anidada?**
   - a. Una variante de K-fold con menos pliegues
   - b. Un bucle interno para hiperparámetros y externo para evaluación ✓
   - c. Entrenar con menos datos para ahorrar tiempo

6. **¿Qué refleja el término "fuga de información"?**
   - a. Baja precisión por desbalance
   - b. Uso indebido de datos de validación o futuro en entrenamiento ✓
   - c. Pérdida de datos durante el entrenamiento

7. **¿Qué sucede si el error de entrenamiento es muy bajo pero validación sigue alto?**
   - a. Subajuste
   - b. Sobreajuste ✓
   - c. Modelo balanceado

8. **¿Qué parámetro se ajustó en el video para evitar que el árbol se sobreajuste?**
   - a. Learning rate
   - b. Máxima profundidad del árbol ✓
   - c. Número de pliegues

9. **En validación cruzada con K=10 y dataset de 500 ejemplos, ¿cuántos se usan para entrenamiento en cada ronda?**
   - a. 100
   - b. 50
   - c. 450 ✓

10. **Un modelo obtiene RMSE en entrenamiento = 5 y en prueba = 5.2. ¿Qué diagnóstico es más probable?**
	- a. Subajuste
	- b. Sobreajuste
	- c. Buen ajuste y generalización ✓

11. **Un modelo lineal aplicado a un problema no lineal suele presentar:**
	- a. Sobreajuste
	- b. Alta varianza
	- c. Subajuste ✓

12. **¿Qué métrica NO es adecuada en un dataset desbalanceado?**
	- a. Accuracy ✓
	- b. F1-score
	- c. Recall

13. **Un modelo obtiene error de entrenamiento 10 % y error de validación 9 %. ¿Cuál es la interpretación?**
	- a. Subajuste
	- b. Sobreajuste
	- c. Modelo generaliza adecuadamente ✓

14. **Si accuracy = 95 % pero recall = 40 %, ¿qué problema refleja?**
	- a. Subajuste
	- b. Desbalance y sobreajuste a la clase mayoritaria ✓
	- c. Validación cruzada

15. **¿Cuál de los siguientes síntomas refleja sobreajuste?**
	- a. Ambos errores altos
	- b. Error bajo en entrenamiento pero alto en validación ✓
	- c. Error alto en entrenamiento y validación

16. **Un dataset tiene 1000 instancias con 20 % positivos. Si se divide en 70 % entrenamiento, 15 % validación y 15 % prueba de forma estratificada, ¿cuántos positivos quedan en validación?**
	- a. 30
	- b. 30 ✓
	- c. 150

17. **¿Qué caracteriza a la validación cruzada K-fold?**
	- a. Usa siempre el mismo corte de datos
	- b. Divide en K pliegues y rota validación ✓
	- c. Entrena con todo y valida con todo

18. **¿Qué sucede cuando se aplica dropout en una red neuronal?**
	- a. Se desactivan aleatoriamente durante entrenamiento ✓
	- b. Se eliminan definitivamente neuronas
	- c. Se reducen los datos de entrada

## Actividades

- [ ] Practicar una división 70/15/15 y explicar para qué sirve cada parte.
- [ ] Resolver ejercicios de k-fold cross-validation.
- [ ] Dibujar un ejemplo de curva de entrenamiento y validación para detectar sobreajuste.
- [ ] Explicar con tus palabras la diferencia entre sobreajuste y subajuste.
- [ ] Identificar qué técnica usarías para corregir cada problema.


