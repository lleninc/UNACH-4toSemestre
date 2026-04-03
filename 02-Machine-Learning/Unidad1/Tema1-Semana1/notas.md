# 02-Machine-Learning - U1 T1 S1

## 🎯 Objetivo de la Unidad
Primera aproximación al fascinante mundo del aprendizaje automático, integrando teoría y práctica para resolver problemas reales con datos. Aprenderás a diseñar, entrenar y evaluar modelos, comprendiendo alcances y limitaciones.

---

## 📚 Tema 1: Introducción y Fundamentos

### 1.1 Concepto y Tipos de Aprendizaje Automático

**Definición clave:**
El aprendizaje automático (ML) es la disciplina que desarrolla algoritmos capaces de mejorar su desempeño en tareas específicas a partir de datos, **sin ser programados explícitamente para cada caso** (ISO, 2023).

**Los 5 Tipos principales de ML:**

| Tipo | Descripción | Aplicaciones |
|------|-------------|--------------|
| **1. Supervisado** | Usa datos con etiquetas conocidas | Clasificación de imágenes, predicción de valores, diagnóstico médico |
| **2. No supervisado** | Datos sin etiquetas, identifica estructuras ocultas | Segmentación de clientes, análisis de redes sociales |
| **3. Semi-supervisado** | Combina pocos datos etiquetados + muchos sin etiquetar | Genómica, contextos donde etiquetado manual es costoso |
| **4. Por refuerzo** | Entrena agentes mediante interacción con entorno (recompensas/penalizaciones) | Robótica, videojuegos complejos |
| **5. Auto-supervisado** | Crea etiquetas artificiales a partir de los propios datos | Modelos de lenguaje grandes (LLMs), visión por computadora |

**Punto importante:** Existen sistemas **híbridos** que combinan lo mejor de cada paradigma para arquitecturas más robustas.

---

### 1.1.1 Detalle Visual de los 5 Tipos de Aprendizaje Automático

** 1. APRENDIZAJE SUPERVISADO**
- **Definición:** Utiliza conjuntos de datos con etiquetas conocidas. El modelo aprende a predecir salidas a partir de ejemplos ya clasificados.
- **Visualización:** Datos de entrada etiquetados (ej: imágenes de gatos  "gato" )
- **Proceso:** Aprende la relación entrada  salida conocida
- **Ejemplo:** Clasificar emails como "spam" o "no spam"
- **Desafío:** Requiere muchos datos etiquetados (costoso)

** 2. APRENDIZAJE NO SUPERVISADO**
- **Definición:** Trabaja con datos sin etiquetas, descubriendo patrones, agrupamientos o estructuras ocultas.
- **Visualización:** Puntos dispersos sin clasificar  agrupados en clusters
- **Proceso:** Encuentra relaciones y similitudes por sí solo
- **Ejemplo:** Segmentar clientes por comportamiento de compra
- **Desafío:** Difícil evaluar si los patrones encontrados son correctos

** 3. APRENDIZAJE SEMI-SUPERVISADO**
- **Definición:** Combina un pequeño conjunto de datos etiquetados con un gran volumen de datos sin etiquetar.
- **Visualización:** Pocos datos etiquetados + muchos sin etiquetar = mejor generalización
- **Proceso:** Usa datos etiquetados para guiar el aprendizaje en datos sin etiquetar
- **Ejemplo:** Genómica con pocos genes clasificados manualmente
- **Desafío:** Balance entre ambos tipos de datos

** 4. APRENDIZAJE AUTO-SUPERVISADO** 
- **Definición:** Genera etiquetas artificiales a partir de los propios datos. Es fundamental en grandes modelos de lenguaje.
- **Visualización:** Documentos/imágenes  crea sus propias etiquetas  aprende representaciones
- **Proceso:** Enmascarar parte del dato y predecir qué falta
- **Ejemplo:** ChatGPT, BERT, GPT-3 predicen la siguiente palabra
- **Desafío:** Diseñar buenas tareas de auto-supervisión

** 5. APRENDIZAJE POR REFUERZO**
- **Definición:** Entrena agentes mediante la interacción con un entorno, recibiendo recompensas (+1) o penalizaciones (-1).
- **Visualización:** Agente  Entorno (acción  recompensa/castigo)
- **Proceso:** Aprende qué acciones maximizan la recompensa acumulada
- **Ejemplo:** Robots, videojuegos AlphaGo, conducción autónoma
- **Desafío:** Definir correctamente la función de recompensa

---

### 1.2 Aplicaciones y Desafíos en Ciencia e Ingeniería

**Aplicaciones Reales (Espectro de uso):**

🏥 **Salud y Biomedicina**
- Diagnóstico asistido por imágenes médicas
- Predicción de riesgos cardiovasculares
- Descubrimiento de fármacos mediante simulaciones moleculares

🏗️ **Ingeniería Civil y Ambiental**
- Detección de fallas estructurales
- Predicción de deslizamientos de tierra
- Modelado de inundaciones desde datos satelitales

📡 **Telecomunicaciones**
- Detección de fraudes
- Predicción de congestión de red
- Optimización de asignación de recursos

📖 **Educación Personalizada**
- Sistemas que adaptan contenidos según desempeño del estudiante
- Itinerarios de aprendizaje flexibles

**Desafíos Críticos (Bajo la superficie):**

| Desafío | Descripción | Impacto |
|---------|-------------|--------|
| **Sesgos y equidad** | Algoritmos reproducen sesgos de los datos | Retos éticos y sociales (Mersha et al., 2024) |
| **Complejidad computacional** | Modelos profundos requieren GPU/TPU | Alto consumo energético (Hao et al., 2022) |
| **Calidad de datos** | Ruido, valores faltantes, distribuciones no representativas | Compromete validez de modelos (Dritsas et al., 2025) |
| **Interpretabilidad** | Necesidad de modelos explicables | Crítico en medicina y finanzas (Mersha et al., 2024) |

**Soluciones emergentes:**
- IA Explicable (XAI - Explainable AI)
- Machine Learning informado por principios físicos (Physics-Informed ML)

---

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

## 🔑 Conceptos Clave para Recordar

1. **ML aprende patrones sin código explícito**
2. **Cada tipo de ML tiene un propósito diferente:** elige según tu problema
3. **Los datos son lo más importante** → calidad > cantidad
4. **Sesgos y ética son fundamentales** en cualquier solución
5. **Las matemáticas son la base** de todo algoritmo
6. **Python + librerías específicas** son la herramienta estándar

---

## 💡 Estrategia de Estudio para la Clase del Lunes (18:00-20:00)

### Antes de la clase:
- [ ] Lee completo esta sección 1.1 (Concepto y tipos)
- [ ] Memoriza los 5 tipos de ML con un ejemplo cada uno
- [ ] Revisa las aplicaciones reales (van a preguntar)

### Durante la clase:
- Toma notas de ejemplos específicos que mencione el profesor
- Pregunta casos de uso en Ecuador o Latinoamérica
- Identifica qué tipo de ML se usa en problemas locales

### Después de la clase:
- [ ] Resume en tus palabras cada desafío (sección 1.2)
- [ ] Investiga: ¿cuál es la barrera más grande para IA en Ecuador?
- [ ] Instala Python + librerías (si no lo has hecho)

---

## 📖 Bibliografía Principal

- IBM. (2023). Five machine learning types to know
- ISO. (2023). Artificial intelligence — Machine learning — Framework
- Mersha, M., et al. (2024). Explainable artificial intelligence: A survey
- Hao, Z., et al. (2022). Physics-informed machine learning: A survey
- Dritsas, E., et al. (2025). Exploring the intersection of machine learning and big data
- Symeonidis, G., et al. (2022). MLOps-definitions, tools and challenges

---

## Notas de clase

## 📝 Quiz - U1 T1 S1

### Pregunta 1: Hitos en IA durante los 2010s

**Pregunta:** ¿Cuál fue un hito en IA en los 2010s?

**Opciones:**
- ❌ El uso de reglas lógicas en todo sistema
- ❌ La exclusión de datos no estructurados
- ✅ **El éxito de redes profundas en visión y lenguaje**

**Análisis - Por qué es correcta:**

En los 2010s ocurrieron eventos históricos que revolucionaron IA:

| Evento | Año | Impacto |
|--------|-----|--------|
| AlexNet gana ImageNet | 2012 | Revoluciona visión por computadora con CNNs profundas |
| Transformers (Attention is All You Need) | 2017 | Base de GPT, BERT, y modelos modernos |
| GPT-2 y GPT-3 | 2018-2020 | Avance masivo en procesamiento de lenguaje natural |
| Deep Learning dominante | 2010-2019 | Se convierte en herramienta estándar de la industria |

**Por qué las otras son incorrectas:**
- **"Reglas lógicas en todo sistema"** → Eso fue en los 1980s-1990s (era simbólica/experta)
- **"Exclusión de datos no estructurados"** → Es lo opuesto | Los 2010s revolucionaron el uso de imágenes, texto, video

**Lección clave:** Los 2010s marcaron la transición de la IA simbólica a la IA basada en aprendizaje profundo.

---

### Pregunta 2: Calidad de Datos en Machine Learning

**Pregunta:** ¿Qué significa la calidad de datos en ML?

**Opciones:**
- ✅ **a) Que ruido y valores faltantes afectan la validez del modelo**
- ❌ b) Que basta con tener grandes volúmenes sin importar su fiabilidad
- ❌ c) Que los modelos pueden aprender incluso sin datos

**Análisis - Por qué es correcta:**

La **calidad de datos es uno de los desafíos críticos de ML** (Dritsas et al., 2025).

**Componentes de calidad de datos:**

| Aspecto | Impacto en el modelo |
|--------|----------------------|
| **Ruido en datos** | Introduce errores aleatorios que el modelo aprende como si fueran patrones reales |
| **Valores faltantes** | Reduce información disponible y puede sesgar el aprendizaje |
| **Distribuciones no representativas** | El modelo no generaliza bien a datos nuevos (nunca visto) |
| **Datos inconsistentes** | Contradicciones que confunden al algoritmo |

**Fórmula importante:**
```
Calidad del modelo = Algoritmo INTELIGENTE + Datos DE CALIDAD
```

Puedes tener el mejor algoritmo del mundo, pero si alimentas un modelo con datos basura, el resultado será "basura dentro, basura fuera" (Garbage In, Garbage Out - GIGO).

**Por qué las otras son incorrectas:**

❌ **"Basta con grandes volúmenes sin importar fiabilidad"**
- Esto es lo OPUESTO a calidad de datos
- Es el concepto de "Big Data" pero sin rigor
- **Cantidad ≠ Calidad**
- Ejemplo: 1 millón de registros con 90% errores < 10,000 registros limpios

❌ **"Los modelos pueden aprender sin datos"**
- Imposible. ML **requiere datos** para aprender patrones
- Sin datos = Sin aprendizaje
- Este es un concepto fundamental

**Lección clave:** "La mayor parte del trabajo en ML es preparación y limpieza de datos, no modelado" (80/20 rule)

---

### Pregunta 3: Aprendizaje No Supervisado

**Pregunta:** ¿En qué consiste el aprendizaje no supervisado?

**Opciones:**
- ❌ a) Depende de etiquetas predefinidas.
- ✅ **b) Identifica estructuras ocultas en datos sin etiquetas.**
- ❌ c) No requiere procesamiento computacional.

**Análisis - Por qué es correcta:**

El aprendizaje no supervisado trabaja con datos sin etiquetas y busca patrones ocultos, como grupos o relaciones.

**Lección clave:** No supervisado = descubrir estructura en datos sin respuestas previas.

---

### Pregunta 4: Definicion de Aprendizaje Automatico (ML)

**Pregunta:** ¿Qué se entiende por aprendizaje automático (ML)?

**Opciones:**
- ❌ a) Algoritmos que solo ejecutan instrucciones predefinidas.
- ✅ **b) Algoritmos que mejoran su desempeño en tareas específicas a partir de datos.**
- ❌ c) Sistemas que reemplazan completamente a los humanos en cualquier tarea.

**Analisis - Por que es correcta:**

El ML se define como el campo que crea algoritmos capaces de **aprender de datos** y **mejorar su desempeño** en tareas concretas sin programar cada regla manualmente.

**Por que las otras son incorrectas:**
- La opcion **a)** describe software tradicional basado en reglas fijas.
- La opcion **c)** exagera el alcance de la IA; ML no reemplaza a humanos en "cualquier" tarea.

**Leccion clave:** ML = aprender patrones desde datos para mejorar resultados en tareas especificas.

---

### Pregunta 5: Aplicacion de ML en Ingenieria Civil y Ambiental

**Pregunta:** En ingenieria civil y ambiental, el ML puede usarse para:

**Opciones:**
- ❌ Traduccion automatica de textos.
- ❌ Crear contenido multimedia.
- ✅ **Prediccion de deslizamientos e inundaciones.**

**Analisis - Por que es correcta:**

En este campo, ML se aplica a problemas de riesgo y territorio usando datos historicos, climaticos y geoespaciales para anticipar eventos.

**Ejemplos tipicos:**
- Prediccion de deslizamientos de tierra.
- Modelado de inundaciones con datos satelitales.
- Deteccion temprana de fallas en infraestructura.

**Por que las otras son incorrectas en este contexto:**
- **Traduccion automatica de textos** pertenece mas a NLP.
- **Crear contenido multimedia** corresponde a IA generativa, no a la aplicacion civil/ambiental planteada.

**Leccion clave:** En civil y ambiental, ML destaca en prediccion de riesgos y apoyo a la toma de decisiones preventivas.

---

### Resumen del Cuestionario Completo

| Pregunta | Respuesta correcta |
|----------|--------------------|
| 1. Hitos en IA en los 2010s | El éxito de redes profundas en visión y lenguaje |
| 2. Calidad de datos en ML | Ruido y valores faltantes afectan la validez del modelo |
| 3. Aprendizaje no supervisado | Identifica estructuras ocultas en datos sin etiquetas |
| 4. Qué es ML | Algoritmos que mejoran su desempeño a partir de datos |
| 5. Uso en civil y ambiental | Predicción de deslizamientos e inundaciones |

**Tip de estudio rápido:** memoriza primero las 5 respuestas correctas de la tabla y luego repasa los análisis de cada pregunta.

---

## Actividades



