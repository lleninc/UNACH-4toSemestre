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

## Quiz

## Actividades

