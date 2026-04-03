# 02-Machine-Learning - U1 T1 S2

## Notas de clase

### 1.3 Fundamentos Matemáticos: Álgebra Lineal, Probabilidad y Estadística

**El éxito de ML se sustenta en estos 3 pilares:**

**📐 Álgebra Lineal**
- Herramientas para representar datos en **vectores y matrices**
- Manipulación de transformaciones lineales
- Descomposiciones (SVD, PCA)
- Avances recientes: Álgebra lineal aleatorizada para datos masivos

**📊 Probabilidad**
- Modelación de la **incertidumbre** mediante distribuciones
- Procesos estocásticos
- Modelos de Markov (esenciales en aprendizaje por refuerzo)
- Teorema de Bayes y razonamiento probabilístico

**📈 Estadística**
- Métodos de **inferencia** y validación
- Pruebas de hipótesis
- Asegurar que modelos sean **generalizables**
- Evitar patrones espurios

**Integración:** Estas disciplinas permiten diseñar algoritmos robustos que equilibren **precisión, eficiencia y capacidad de generalización**.

---

### 1.4 Herramientas Computacionales

**Ecosistema tecnológico para desarrollo práctico:**

**🐍 Lenguajes de Programación**
- **Python** domina el campo (simplicidad + extensa librería)

**📦 Bibliotecas Científicas**
- **NumPy:** Manipulación de datos numéricos
- **Pandas:** Análisis y manipulación de datos
- **Matplotlib & Seaborn:** Visualización
- **Scikit-learn:** Modelos clásicos de ML

**🧠 Frameworks de Deep Learning**
- **TensorFlow:** Construcción y entrenamiento de redes neuronales profundas
- **PyTorch:** Framework flexible para modelos complejos

**💻 Entornos Interactivos**
- **Jupyter Notebooks:** Documentación reproducible
- **Google Colab:** Ejecución en la nube

**⚙️ Prácticas de MLOps**
- Integración de ingeniería de software + ciencia de datos
- Reproducibilidad y escalabilidad en producción

---

### 1.4.1 Repaso Visual de Herramientas Computacionales

**Texto clave de la actividad:** El desarrollo práctico de proyectos de Machine Learning se apoya en un ecosistema tecnologico diverso.

| Herramienta | Funcion principal | Uso en ML |
|-------------|-------------------|-----------|
| Python | Lenguaje de programacion mas utilizado | Programar modelos y flujos de trabajo |
| NumPy | Computacion numerica | Operar con arreglos y matrices |
| Pandas | Manipulacion de datos tabulares | Cargar, limpiar y analizar DataFrames |
| Matplotlib | Visualizacion de datos | Crear graficas y reportes visuales |
| Scikit-learn | ML clasico | Clasificacion, regresion y clustering |
| TensorFlow | Deep learning | Construir y entrenar redes neuronales profundas |
| PyTorch | Deep learning flexible | Prototipado y entrenamiento de modelos |
| Jupyter | Entorno interactivo | Documentar y ejecutar experimentos |
| Colab | Entorno en la nube | Ejecutar notebooks sin instalar localmente |

**Idea principal:** Cada herramienta cumple una funcion distinta dentro del flujo de trabajo de ML: cargar datos, analizarlos, visualizarlos, modelar y documentar experimentos.

## Quiz

### Pregunta 1: Ejemplo clasico de aprendizaje supervisado

**Pregunta:** ¿Cual es un ejemplo clasico de aprendizaje supervisado?

**Opciones:**
- ❌ Agrupar clientes sin etiquetas
- ✅ **Filtrar correos como spam o no spam**
- ❌ Generar imagenes sinteticas sin datos reales

**Analisis - Por que es correcta:**

El filtrado de spam es aprendizaje supervisado porque se entrena con correos ya etiquetados como "spam" y "no spam".

**Por que las otras son incorrectas:**
- "Agrupar clientes sin etiquetas" corresponde a aprendizaje no supervisado (clustering).
- "Generar imagenes sinteticas" pertenece a modelos generativos, no al ejemplo clasico de clasificacion supervisada.

---

### Pregunta 2: Probabilidad y modelos de Markov

**Pregunta:** ¿Que relacion tiene la probabilidad con los modelos de Markov?

**Opciones:**
- ✅ **Modelan procesos estocasticos y secuenciales**
- ❌ Representan datos deterministas
- ❌ Solo sirven en algebra lineal

**Analisis - Por que es correcta:**

Los modelos de Markov usan probabilidad para describir transiciones entre estados en el tiempo. Por eso modelan procesos estocasticos y secuenciales.

**Por que las otras son incorrectas:**
- "Datos deterministas" no requieren modelado probabilistico.
- No se limitan al algebra lineal; pertenecen sobre todo a probabilidad y procesos estocasticos.

---

### Pregunta 3: Por que Python es preferido en ML

**Pregunta:** ¿Por que Python es preferido en proyectos de machine learning?

**Opciones:**
- ❌ Porque es el unico lenguaje que permite condicionales.
- ✅ **Porque es simple de aprender y tiene un ecosistema amplio de librerias cientificas.**
- ❌ Porque no requiere bibliotecas externas.

**Analisis - Por que es correcta:**

Python destaca en ML por su sintaxis accesible y por su ecosistema maduro: NumPy, Pandas, Scikit-learn, TensorFlow y PyTorch.

**Por que las otras son incorrectas:**
- Todos los lenguajes de programacion modernos permiten condicionales.
- Python si depende de bibliotecas externas para ciencia de datos y ML.

**Leccion clave:** Python es preferido por productividad + comunidad + librerias especializadas.

---

### Pregunta 4: Funcion de pandas

**Pregunta:** ¿Cual es la funcion de pandas?

**Opciones:**
- ❌ Crear redes neuronales profundas.
- ✅ **Manipular y analizar datos en tablas (DataFrames).**
- ❌ Renderizar graficos 3D.

**Analisis - Por que es correcta:**

Pandas es una libreria para carga, limpieza, transformacion y analisis de datos tabulares usando estructuras como Series y DataFrames.

**Por que las otras son incorrectas:**
- Crear redes neuronales profundas corresponde a TensorFlow o PyTorch.
- Renderizado 3D no es el foco principal de pandas.

**Leccion clave:** Pandas = trabajo eficiente con datos tabulares en ML.

---

### Pregunta 5: Papel del algebra lineal en ML

**Pregunta:** ¿Que papel cumple el algebra lineal en el aprendizaje automatico?

**Opciones:**
- ✅ **Permite representar datos en vectores y matrices y aplicar transformaciones lineales**
- ❌ Define reglas de logica simbolica
- ❌ Facilita la edicion de imagenes en alta resolucion

**Analisis - Por que es correcta:**

El algebra lineal es base de ML porque permite modelar datos y operaciones como productos matriciales, proyecciones y descomposiciones (por ejemplo, PCA y SVD).

**Por que las otras son incorrectas:**
- La logica simbolica pertenece a otro enfoque de IA, no al nucleo matematico de ML moderno.
- La edicion de imagenes no describe el rol matematico del algebra lineal en entrenamiento de modelos.

**Leccion clave:** Sin algebra lineal no se pueden representar ni transformar eficientemente los datos en ML.

## Actividades

