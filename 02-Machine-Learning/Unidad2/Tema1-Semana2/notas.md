# 02-Machine-Learning - U2 T1 S2

## Notas de clase

### 1.3. Máquinas de Soporte Vectorial (SVM)

#### Concepto fundamental
Las Máquinas de Soporte Vectorial (SVM) resuelven el problema de clasificación buscando el hiperplano que deja el mayor margen entre las clases. El margen (la distancia a los puntos más cercanos de cada clase, llamados vectores de soporte) actúa como un "colchón de seguridad": cuanto mayor, más robusta suele ser la separación frente a ruido y nuevas observaciones.

#### SVM Lineal
En su forma más simple, una SVM lineal aprende una función de decisión afín:

**Modelo:**
- f(x) = wᵀx + b
- La clase predicha depende del signo de f(x)

**Optimización:**
- Minimizar: 1/2 ||w||² + C Σ ξᵢ
- Sujeto a restricciones de separación con holguras ξᵢ
- El hiperparámetro C regula el compromiso entre margen amplio y errores de entrenamiento

**Interpretación de C:**
- **C grande:** penaliza fuertemente los errores de entrenamiento → posible sobreajuste (margen estrecho, fronteras rígidas)
- **C pequeño:** tolera más errores a cambio de margen amplio → riesgo de subajuste

#### SVM No Lineal: Funciones Kernel
Muchos problemas no son linealmente separables en el espacio original de características. Las SVM solucionan esto con funciones kernel que proyectan implícitamente los datos a un espacio de mayor dimensión.

**El "truco del kernel":**
- Nunca calculamos la proyección de forma explícita
- Solo evaluamos similitudes entre pares de puntos
- Reduce costo computacional drásticamente

**Kernels frecuentes:**

1. **Kernel Lineal:** cuando una frontera plana es suficiente
2. **Kernel Polinomial:** introduce interacciones y curvaturas de orden mayor
   - Fórmula: K(x, y) = (xᵀy + 1)^d
3. **Kernel RBF (Radial Basis Function):** muy usado; crea fronteras suavemente curvas
   - Fórmula: K(x, y) = e^(-γ||x-y||²)
4. **Kernel Sigmoide:** emparentado con neuronas artificiales (menos popular que RBF)

#### Hiperparámetro γ (gamma) en RBF
Con RBF, aparece el hiperparámetro γ que controla el "alcance" de cada muestra en la frontera:

- **γ alto:** influencia localizada → fronteras muy onduladas (varianza alta, riesgo de sobreajuste)
- **γ bajo:** influencia amplia → fronteras suaves (sesgo alto, riesgo de subajuste)

#### Ajuste de hiperparámetros
Una regla fundamental: ajustar C y γ de manera conjunta, preferentemente mediante validación cruzada:

- C regula el equilibrio entre margen amplio y errores en entrenamiento
- γ controla la complejidad de la frontera de decisión (en RBF)
- Ambos interactúan entre sí
- No existe un valor universalmente mejor; depende de los datos

#### Aplicaciones típicas de SVM
- **Clasificación de texto e imágenes:** con representaciones como bolsa de palabras o descriptores visuales
- **Diagnóstico médico:** detección de tumores a partir de imágenes biomédicas
- **Bioinformática:** análisis de expresión génica o estudios proteómicos
- **Detección de fraude financiero:** identificación de transacciones anómalas

---

### 1.4. Redes Neuronales Básicas

#### Inspiración biológica
Las redes neuronales artificiales (RNA) se inspiran en la neurona biológica, pero operan con una formulación matemática controlable y entrenable. Su fuerza radica en aprender representaciones no lineales de los datos componiendo transformaciones simples en capas.

#### Neurona artificial
Cada neurona realiza una combinación lineal con sesgo y la pasa por una función de activación:

**Modelo:**
- z = Σ wᵢ xᵢ + b
- a = σ(z)
- Donde x = (x₁, ..., xₙ) es el vector de entrada
- w = (w₁, ..., wₙ) son los pesos
- b es el sesgo (bias)
- σ(·) es la función de activación

#### Funciones de Activación
La no linealidad σ es imprescindible para que la red pueda aprender relaciones complejas:

1. **Sigmoide:** σ(z) = 1/(1 + e⁻ᶻ)
   - Útil para probabilidades (clasificación binaria)
   - Desventaja: se satura, degradando gradientes

2. **Tanh:** σ(z) = (eᶻ - e⁻ᶻ)/(eᶻ + e⁻ᶻ)
   - Centrada en 0
   - Ayuda a la estabilidad del entrenamiento

3. **ReLU:** σ(z) = max(0, z)
   - Estándar en redes modernas
   - Eficiente computacionalmente
   - Mejor propagación de gradientes

#### Arquitectura de Red Neuronal
Una red típica se organiza en tres niveles:

1. **Capa de entrada:** recibe el vector de características x
2. **Capas ocultas:** generan representaciones intermedias mediante funciones de activación
3. **Capa de salida:** produce la predicción final ŷ

**Descripción matemática:**
- a⁽ˡ⁾ = σ(W⁽ˡ⁾a⁽ˡ⁻¹⁾ - b⁽ˡ⁾)
- Donde W⁽ˡ⁾ y b⁽ˡ⁾ son los parámetros entrenables de la capa l

#### Aprendizaje: Retropropagación
El proceso de aprendizaje se lleva a cabo mediante retropropagación y optimización iterativa:

**Retropropagación:**
- Aplica la regla de la cadena para calcular gradientes
- Calcula derivadas de la función de pérdida respecto a cada parámetro

**Optimizadores:**
- **SGD (Descenso por Gradiente Estocástico):** actualización simple
- **Adam:** adaptativo, converge más rápido, muy usado actualmente
- Se ajustan W⁽ˡ⁾ y b⁽ˡ⁾ en ciclos denominados épocas hasta lograr convergencia

#### Regularización y validación
Para garantizar la convergencia y evitar sobreajuste:

1. **Escalado de variables:** normalizar variables de entrada
2. **Early stopping:** detener cuando validación no mejora
3. **Weight decay:** penalizar pesos grandes (similar a Ridge)
4. **Dropout:** desactivar aleatoriamente neuronas durante entrenamiento

#### Relación sesgo-varianza
Aspecto fundamental para entender redes neuronales:

- **Redes con pocas neuronas:** alto sesgo (subajuste), no aprenden patrones complejos
- **Redes grandes sin regularización:** alta varianza (sobreajuste), memorizan datos

#### Calibración de probabilidades
En aplicaciones sensibles (diagnóstico médico), la confiabilidad de las predicciones es tan importante como la exactitud. Las probabilidades predichas deben reflejar la incertidumbre real.

#### Aplicaciones típicas
- **Clasificación de imágenes:** MNIST, CIFAR (dígitos, objetos)
- **Procesamiento de texto:** análisis de sentimientos, clasificación de noticias
- **Predicción de series temporales:** análisis de tendencias financieras
- **Reconocimiento de voz:** transcripción automática

#### Comparación SVM vs Redes Neuronales

| Aspecto | SVM | Redes Neuronales |
|---------|-----|------------------|
| Datos pequeños/medianos | Excelente | Puede sobreajustar |
| Datos grandes | Moderado | Excelente |
| Interpretabilidad | Alta (vectores de soporte) | Baja (caja negra) |
| Velocidad entrenamiento | Rápida | Lenta (requiere GPU) |
| Ingeniería de features | Crítica | Automática (aprende representaciones) |
| Flexibilidad | Media (kernel fijo) | Alta (arquitectura configurable) |

#### Errores comunes y buenas prácticas

**Errores a evitar:**
- No escalar variables antes de entrenar
- Seleccionar hiperparámetros usando conjunto de prueba (sesgo optimista)
- Confundir rendimiento en entrenamiento con capacidad de generalización

**Buenas prácticas:**
- Usar siempre validación cruzada
- Interpretar modelos según sus particularidades (vectores de soporte en SVM, curvas de entrenamiento en MLP)
- Discutir el dilema sesgo-varianza como criterio para elegir modelos
- Documentar arquitectura y ajustes de hiperparámetros

---

## Quiz

### Preguntas de repaso:

1. **¿Cuál es el objetivo principal de las SVM?**
   - a. Maximizar el error de clasificación
   - b. Buscar el hiperplano con mayor margen entre clases ✓
   - c. Minimizar el número de características

2. **¿Qué son los vectores de soporte en SVM?**
   - a. Los puntos más alejados de la frontera de decisión
   - b. Los puntos más cercanos a la frontera de decisión ✓
   - c. Puntos seleccionados aleatoriamente

3. **El kernel RBF en SVM es útil cuando:**
   - a. Los datos son perfectamente separables linealmente
   - b. Los datos no son linealmente separables ✓
   - c. No hay suficientes datos

4. **¿Qué significa γ (gamma) alto en SVM con kernel RBF?**
   - a. Fronteras suaves (bajo sesgo)
   - b. Fronteras onduladas, muy localizadas (alto riesgo de sobreajuste) ✓
   - c. Mayor generalización

5. **En una red neuronal, ¿cuál es el propósito de la función de activación?**
   - a. Escalar linealmente los datos
   - b. Introducir no linealidad para aprender relaciones complejas ✓
   - c. Normalizar los pesos

6. **¿Cuál es la función de activación estándar en redes modernas?**
   - a. Sigmoide
   - b. Tanh
   - c. ReLU ✓

7. **¿Qué hace la retropropagación en una red neuronal?**
   - a. Propaga datos hacia adelante
   - b. Calcula gradientes de la función de pérdida para actualizar parámetros ✓
   - c. Escala las variables de entrada

8. **Una red neuronal con pocas neuronas tiende a:**
   - a. Sobreajustar (alta varianza)
   - b. Subajustar con alto sesgo ✓
   - c. Tener mejor generalización

9. **¿Para qué se utiliza Dropout en redes neuronales?**
   - a. Para acelerar el entrenamiento
   - b. Para reducir sobreajuste desactivando aleatoriamente neuronas ✓
   - c. Para aumentar la precisión

10. **¿Cuándo es mejor usar SVM sobre redes neuronales?**
    - a. Siempre son superiores las redes neuronales
    - b. Con datasets pequeños/medianos y cuando interpretabilidad es importante ✓
    - c. SVM es siempre mejor

### QUIZ U2-T1-S2 (APE6) — Extraído de PDFs

Fuentes: 
- QUIZ U2-T1-S2 (APE6)_Machine Learning.pdf
- QUIZ U2-T1-S2 (APE6)_MachineLearning_LL.pdf
- QUIZ U2-T1-S2 (APE6)_MachineLearning_LL1.pdf

1. **¿Qué algoritmo de optimización es alternativa al SGD clásico?**
   - a. Newton-Raphson
   - b. Backtracking
   - c. Adam ✓

2. **¿Qué kernel se relaciona conceptualmente con las neuronas artificiales?**
   - a. Polinomial
   - b. RBF
   - c. Sigmoide ✓

3. **En problemas de texto, ¿qué representación se usa frecuentemente con SVM?**
   - a. Cadenas de Markov
   - b. Redes convolucionales
   - c. Bolsa de palabras (bag of words) ✓

4. **¿Qué función de pérdida es común en clasificación con redes neuronales?**
   - a. MSE
   - b. Entropía cruzada ✓
   - c. Log-loss

5. **¿Qué mide la función f(x)=w?x+b en SVM?**
   - a. La distancia al hiperplano ✓
   - b. El número de vectores de soporte
   - c. La probabilidad de clase

6. **¿Qué kernel es más adecuado cuando los datos son linealmente separables?**
   - a. Kernel RBF
   - b. Kernel polinomial
   - c. Kernel lineal ✓

7. **¿Qué ocurre si se seleccionan hiperparámetros usando el conjunto de prueba?**
   - a. Mejora generalización
   - b. No tiene consecuencias
   - c. Se produce fuga de información y evaluación optimista ✓

8. **¿Qué salida produce una capa Softmax en redes neuronales?**
   - a. Probabilidades normalizadas multiclase ✓
   - b. Valores entre -1 y 1
   - c. Distancias al hiperplano

9. **¿Qué función de activación es estándar en redes modernas por su eficiencia?**
   - a. Sigmoide
   - b. Tanh
   - c. ReLU ✓

10. **¿Cuál es el rol de los vectores de soporte en SVM?**
   - a. Son los puntos más cercanos al hiperplano que definen la frontera ✓
   - b. Son los puntos más alejados del hiperplano
   - c. Son todos los puntos de entrenamiento

11. **¿Qué busca maximizar una SVM lineal al separar clases?**
   - a. El margen entre las clases ✓
   - b. El número de parámetros del modelo
   - c. El número de vectores de soporte

12. **¿Qué función de activación se usa típicamente en clasificación binaria por probabilidades?**
   - a. ReLU
   - b. Tanh
   - c. Sigmoide ✓

13. **¿Qué técnica ayuda a detener el entrenamiento antes del sobreajuste?**
   - a. Expansión de dataset
   - b. Early stopping ✓
   - c. Regularización L1

14. **¿Cuál es una diferencia práctica entre SVM y redes neuronales?**
   - a. SVM requiere más datos
   - b. SVM es más eficiente en datasets pequeños ✓
   - c. RNA es más interpretable

15. **¿Qué combina una neurona artificial antes de aplicar la función de activación?**
   - a. Un producto cruzado entre entradas
   - b. Una resta entre entradas
   - c. Una suma ponderada más un sesgo ✓

16. **¿Qué representa el hiperparámetro C en una SVM?**
   - a. El número de vectores de soporte
   - b. El grado de penalización por errores de entrenamiento ✓
   - c. La tasa de aprendizaje del modelo

17. **¿Qué efecto tiene un gamma (γ) alto en un kernel RBF?**
   - a. Fronteras suaves y generalización amplia
   - b. Fronteras muy onduladas y riesgo de sobreajuste ✓
   - c. Disminución de la dimensionalidad

18. **¿Qué rol tiene el sesgo (b) en una neurona?**
   - a. Aumenta el número de neuronas
   - b. Desplaza la función de activación ✓
   - c. Evita la regularización

19. **¿Qué problema clásico no puede resolver un perceptrón simple?**
   - a. Problema XOR ✓
   - b. Regresión lineal
   - c. Clasificación lineal

20. **¿Qué técnica evita sobreajuste en redes neuronales?**
   - a. Usar siempre sigmoide
   - b. Dropout ✓
   - c. Aumentar neuronas sin límite

---

## Actividades

### Actividad 1: Exploración de Kernels en SVM
Comparar rendimiento de SVM con kernels lineal, polinomial y RBF en un mismo dataset y visualizar fronteras de decisión.

### Actividad 2: Ajuste de Hiperparámetros
Usar GridSearchCV para encontrar los mejores valores de C y γ en SVM mediante validación cruzada.

### Actividad 3: Red Neuronal Básica
Implementar un Perceptrón Multicapa (MLP) en Python con una o dos capas ocultas para clasificación o regresión.

### Actividad 4: Comparación de Modelos
Aplicar SVM, Regresión Logística y Red Neuronal al mismo problema y comparar precisión, tiempo de entrenamiento e interpretabilidad.

