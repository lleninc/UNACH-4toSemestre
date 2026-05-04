# 02-Machine-Learning - U2 T1 S1

## Notas de clase

### 1.1. Regresión lineal, polinómica y regularizada

#### Regresión Lineal
La regresión lineal constituye el punto de partida de los modelos supervisados de predicción. Su propósito es estimar una variable de salida **y** como combinación lineal de un conjunto de predictores x₁, x₂, ..., xₚ.

**Modelo matemático:**
- ŷ = β₀ + Σ βⱼ xⱼ (j=1 a p)
- Donde β₀ es el intercepto y βⱼ son los coeficientes asociados a cada predictor
- El ajuste se logra minimizando el error cuadrático medio (MSE)

**Solución matricial:**
- β = (XᵀX)⁻¹ XᵀY (siempre que X tenga rango completo)

**Interpretabilidad:**
- Los coeficientes muestran cómo cambia la variable dependiente por unidad de cambio en cada predictor
- Supone: relaciones lineales, independencia de errores, homocedasticidad y normalidad de residuos

#### Regresión Polinómica
Cuando la relación entre variables no es lineal, la regresión polinómica amplía la expresividad del modelo introduciendo potencias de los predictores:

**Modelo:**
- ŷ = β₀ + β₁x + β₂x² + ... + βₙxⁿ

**Características:**
- Permite capturar curvaturas y tendencias complejas
- Incrementar el grado p puede generar riesgo de sobreajuste
- Ilustra la tensión sesgo-varianza: bajo grado = alto sesgo, alto grado = alta varianza

#### Regularización (Ridge y Lasso)
La regularización es una estrategia esencial para controlar la complejidad y evitar sobreajuste.

**Ridge (L2) - Penaliza suma de cuadrados:**
- Minimiza: RSS + λ Σ β²ⱼ
- Encoge los coeficientes (los reduce)
- Útil frente a colinealidad
- No anula coeficientes

**Lasso (L1) - Penaliza suma de valores absolutos:**
- Minimiza: RSS + λ Σ |βⱼ|
- Puede anular algunos coeficientes
- Actúa como mecanismo de selección de variables
- Produce modelos más interpretables

**Hiperparámetro λ:**
- Controla la intensidad de la penalización
- Se ajusta mediante validación cruzada
- λ grande = más penalización (mayor sesgo, menor varianza)
- λ pequeño = menos penalización (menor sesgo, mayor varianza)

---

### 1.2. Regresión Logística y Softmax

#### Regresión Logística Binaria
A diferencia de la regresión lineal, la regresión logística está diseñada para resolver problemas de clasificación, no de predicción de valores continuos.

**Modelo matemático:**
- P(y=1|X) = σ(wᵀx + b) = 1/(1 + e⁻⁽ʷᵀˣ⁺ᵇ⁾)
- Donde σ(z) es la función sigmoide
- w es un vector de coeficientes (pesos)
- b es el sesgo (bias o intercepto)
- ŷ es la probabilidad estimada de que la observación pertenezca a la clase positiva

**Función de pérdida - Entropía cruzada:**
- L(w) = -Σ [y log(ŷ) + (1-y) log(1-ŷ)]
- Se minimiza mediante optimización iterativa

**Características:**
- Los coeficientes se interpretan en términos de log-odds
- Muy valorada en ciencias de la salud, economía y marketing
- Proporciona probabilidades de clasificación

#### Softmax (Multiclase)
Cuando el problema incluye más de dos clases, el modelo Softmax generaliza la regresión logística.

**Modelo matemático:**
- P(y=k|X) = e^(wₖᵀx + bₖ) / Σ e^(wⱼᵀx + bⱼ) (j=1 a K)
- Donde K es el número de clases
- wₖ es el vector de pesos para la clase k
- bₖ es el sesgo para la clase k

**Características:**
- Cada observación recibe un vector de probabilidades que suma uno
- Se asigna la clase con mayor probabilidad
- Es la capa de salida estándar en redes neuronales
- Gran eficacia en tareas de clasificación de imágenes y texto

---

## Quiz

### Preguntas de repaso (30 preguntas totales de los 3 quizzes):

#### QUIZ 1 - Preguntas 1-10

1. **El método Lasso (L1) se caracteriza por:**
   - a. Anular algunos coeficientes (selección de variables) ✓
   - b. Calcular probabilidades exactas
   - c. Encoger coeficientes sin anularlos

2. **¿Qué determina la clase predicha en Softmax?**
   - a. El promedio de coeficientes
   - b. La clase con probabilidad más alta ✓
   - c. La suma de errores

3. **La regresión logística es muy usada en:**
   - a. Topología algebraica
   - b. Criptografía avanzada
   - c. Salud, economía y marketing ✓

4. **En regularización, L1 y L2 se diferencian porque:**
   - a. L1 puede anular coeficientes; L2 solo los reduce ✓
   - b. Ninguna afecta los coeficientes
   - c. Ambas siempre anulan coeficientes

5. **¿Qué función se utiliza en la regresión logística binaria?**
   - a. Sigmoide (logística) ✓
   - b. Función identidad
   - c. Tangente hiperbólica

6. **Una diferencia clave entre regresión lineal y logística es:**
   - a. Una usa sigmoide, la otra Softmax
   - b. Una predice valores continuos, la otra probabilidades ✓
   - c. Ambas predicen continuos

7. **Cuando se usa Ridge (L2), la penalización es sobre:**
   - a. La suma de los valores absolutos de los residuos
   - b. La suma de los residuos
   - c. La suma de los cuadrados de los coeficientes ✓

8. **¿Qué supone la regresión lineal sobre los errores?**
   - a. Que sean independientes y homocedásticos ✓
   - b. Que sigan una distribución uniforme
   - c. Que siempre sean positivos

9. **El modelo Softmax generaliza la regresión logística a:**
   - a. Más de dos clases ✓
   - b. Datos faltantes
   - c. Series temporales

10. **El problema del sobreajuste en polinomios se controla mejor con:**
    - a. Reduciendo el tamaño de los datos
    - b. Regularización y validación cruzada ✓
    - c. Aumentando siempre el grado

#### QUIZ 2 - Preguntas 11-20

11. **Softmax es ampliamente usado en:**
    - a. Cálculo de determinantes
    - b. Segmentación de intervalos numéricos
    - c. Redes neuronales como capa de salida ✓

12. **En la regresión logística, los coeficientes w se interpretan como:**
    - a. Desviaciones estándar
    - b. Contribuciones en términos de log-odds ✓
    - c. Promedios muestrales

13. **La función de pérdida usada en regresión logística es:**
    - a. Error cuadrático medio
    - b. Logaritmo natural de los predictores
    - c. Entropía cruzada ✓

14. **¿Cuál es el propósito principal de la regresión lineal?**
    - a. Clasificar variables en categorías
    - b. Estimar una variable de salida en función de predictores ✓
    - c. Calcular probabilidades acumuladas

15. **La regresión polinómica permite:**
    - a. Eliminar multicolinealidad automáticamente
    - b. Capturar relaciones curvas y complejas ✓
    - c. Reducir el número de variables

16. **En un modelo de regresión lineal, ¿qué significa el término constante o intercepto?**
    - a. El error cuadrático medio del ajuste
    - b. El valor estimado de la variable de salida cuando todos los predictores valen cero ✓
    - c. La pendiente de la variable independiente

17. **¿Qué función se utiliza en la regresión logística binaria?**
    - a. Función identidad
    - b. Sigmoide (logística) ✓
    - c. Tangente hiperbólica

18. **El problema del sobreajuste en polinomios se controla mejor con:**
    - a. Aumentando siempre el grado
    - b. Reduciendo el tamaño de los datos
    - c. Regularización y validación cruzada ✓

19. **¿Qué papel cumple el parámetro b en la regresión logística?**
    - a. El grado polinómico
    - b. La tasa de aprendizaje
    - c. El sesgo (bias o intercepto) ✓

20. **En resumen, ¿qué equilibrio buscan los modelos de regresión?**
    - a. Balancear complejidad e interpretabilidad ✓
    - b. Minimizar la dimensionalidad
    - c. Garantizar normalidad absoluta

#### QUIZ 3 - Preguntas 21-30

21. **¿Qué condición debe cumplir la matriz X para que la solución matricial de la regresión lineal sea posible?**
    - a. Que todos los coeficientes sean positivos
    - b. Que tenga rango completo ✓
    - c. Que todos los residuos sean iguales a cero

22. **El método Lasso (L1) se caracteriza por:**
    - a. Anular algunos coeficientes (selección de variables) ✓
    - b. Encoger coeficientes sin anularlos
    - c. Calcular probabilidades exactas

23. **El hiperparámetro λ en regularización controla:**
    - a. La intensidad de la penalización ✓
    - b. La cantidad de observaciones
    - c. El número de variables seleccionadas

24. **¿Qué ocurre si la relación entre variables es no lineal y se usa regresión lineal simple?**
    - a. El modelo ajusta perfectamente los datos
    - b. El modelo presenta alto sesgo ✓
    - c. El modelo mejora la varianza

25. **El modelo Softmax generaliza la regresión logística a:**
    - a. Series temporales
    - b. Datos faltantes
    - c. Más de dos clases ✓

26. **Una diferencia clave entre regresión lineal y logística es:**
    - a. Una usa sigmoide, la otra Softmax
    - b. Ambas predicen continuos
    - c. Una predice valores continuos, la otra probabilidades ✓

27. **La regresión logística con Softmax es útil cuando:**
    - a. Existen múltiples clases posibles ✓
    - b. Hay una sola clase
    - c. Los datos son determinísticos

28. **¿Qué ocurre si λ=0 en Ridge o Lasso?**
    - a. Se obtiene la regresión lineal clásica ✓
    - b. Se eliminan todas las variables
    - c. El modelo se vuelve no lineal

29. **¿Qué riesgo aumenta al incrementar el grado del polinomio?**
    - a. Sobreajuste ✓
    - b. Falta de convergencia numérica
    - c. Sesgo

30. **La regresión logística se utiliza principalmente para:**
    - a. Calcular raíces cuadradas de matrices
    - b. Predecir valores continuos
    - c. Resolver problemas de clasificación ✓

---

## Actividades

### Actividad 1: Análisis de Regularización
Implementar regresión lineal, Ridge y Lasso en Python con un dataset e interpretar cómo cambian los coeficientes según λ.

### Actividad 2: Clasificación con Logística
Aplicar regresión logística a un problema binario y evaluar probabilidades predichas.

### Actividad 3: Softmax Multiclase
Usar Softmax para clasificación de tres o más clases e interpretar las probabilidades por clase.

