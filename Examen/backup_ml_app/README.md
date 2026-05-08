# Sistema de Análisis y Predicción de Jobs de Backup

## 📊 Descripción del Proyecto

Este proyecto implementa un sistema inteligente de análisis y predicción para reducir el número de jobs de backup con error utilizando técnicas de Machine Learning. La aplicación web desarrollada en Flask permite visualizar datos, entrenar modelos y realizar predicciones en tiempo real.

## 🎯 Objetivos

- **Objetivo Principal:** Reducir el número de jobs de backup con error mediante predicción inteligente
- **Objetivos Específicos:**
  - Analizar patrones en datos históricos de backup
  - Identificar factores que contribuyen a los fallos
  - Desarrollar modelos predictivos precisos
  - Crear una aplicación web interactiva
  - Proporcionar recomendaciones de optimización

## 🏗️ Arquitectura del Sistema

```
├── app.py                 # Aplicación Flask principal
├── data_analysis.py       # Módulo de análisis y ML
├── requirements.txt       # Dependencias del proyecto
├── data/
│   └── backup.csv        # Dataset de jobs de backup
├── models/               # Modelos entrenados (generados)
├── templates/            # Plantillas HTML
│   ├── base.html
│   ├── index.html
│   ├── analysis.html
│   ├── train.html
│   ├── predict.html
│   ├── documentation.html
│   └── error.html
└── static/              # Archivos estáticos (CSS, JS, imágenes)
```

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.12** - Lenguaje principal
- **Flask 2.3** - Framework web
- **Pandas 2.1** - Manipulación de datos
- **Scikit-learn 1.3** - Machine Learning
- **NumPy 1.24** - Computación numérica
- **Plotly 5.16** - Visualizaciones interactivas

### Frontend
- **HTML5/CSS3** - Estructura y estilos
- **Bootstrap 5** - Framework de UI
- **JavaScript ES6** - Interactividad
- **jQuery 3.6** - Manipulación DOM
- **Font Awesome** - Iconografía

## 📋 Requisitos del Sistema

- Python 3.8 o superior
- 4GB RAM mínimo (8GB recomendado)
- 500MB espacio en disco
- Navegador web moderno

## 🚀 Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone [URL_DEL_REPOSITORIO]
cd backup_ml_app
```

### 2. Crear Entorno Virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Verificar Datos
Asegúrese de que el archivo `data/backup.csv` esté presente con los datos de backup.

### 5. Ejecutar la Aplicación
```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 📊 Uso del Sistema

### 1. Dashboard Principal
- Vista general del sistema
- Métricas clave
- Estado del modelo
- Navegación a funcionalidades

### 2. Análisis Exploratorio
- Estadísticas descriptivas
- Visualizaciones interactivas
- Distribuciones y patrones
- Insights automatizados

### 3. Entrenamiento de Modelos
- Selección de algoritmos ML
- Proceso de entrenamiento paso a paso
- Evaluación de rendimiento
- Selección del mejor modelo

### 4. Predicciones
- Formulario de entrada de datos
- Predicción en tiempo real
- Probabilidades de riesgo
- Recomendaciones automatizadas

## 🤖 Modelos de Machine Learning

### Algoritmos Implementados

1. **Random Forest**
   - Conjunto de árboles de decisión
   - Excelente para datos mixtos (categóricos + numéricos)
   - Resistente al overfitting
   - Precisión esperada: 87-92%

2. **Gradient Boosting**
   - Mejora iterativa de modelos débiles
   - Alta capacidad predictiva
   - Manejo robusto de patrones complejos
   - Precisión esperada: 85-90%

3. **Logistic Regression**
   - Modelo lineal interpretable
   - Baseline para comparación
   - Rápido entrenamiento e inferencia
   - Precisión esperada: 75-80%

### Métricas de Evaluación

- **Accuracy:** Proporción de predicciones correctas
- **Precision:** Verdaderos positivos / (VP + Falsos positivos)
- **Recall:** Verdaderos positivos / (VP + Falsos negativos)
- **F1-Score:** Media armónica de precision y recall

## 📈 Dataset y Features

### Características del Dataset
- **Registros:** 82,873 jobs de backup
- **Variables:** 13 columnas de información técnica
- **Período:** Datos históricos de sistema corporativo

### Variables Principales
- `Job Id`: Identificador único
- `Type`: Tipo de operación (Backup, Replication, Snapshot)
- `State`: Estado del job (Active, Queued, etc.)
- `KB/Sec`: Velocidad de transferencia
- `Job Policy`: Política aplicada
- `Media Server`: Servidor ejecutor
- `Start Time`: Fecha y hora de inicio
- `Kilobytes`: Tamaño de datos

### Ingeniería de Features
- Extracción de hora y día de la semana
- Categorización de velocidades y tamaños
- Codificación de variables categóricas
- Normalización de variables numéricas
- Creación de variable objetivo `has_error`

## 📋 Metodología

Seguimos el proceso estándar CRISP-DM:

1. **Comprensión del Negocio:** Análisis de requerimientos
2. **Comprensión de Datos:** Exploración y análisis descriptivo
3. **Preparación de Datos:** Limpieza y transformación
4. **Modelado:** Entrenamiento de algoritmos ML
5. **Evaluación:** Validación y selección de modelos
6. **Despliegue:** Implementación en aplicación web

## 🎨 Características de la Interfaz

- **Diseño Responsive:** Compatible con dispositivos móviles
- **Visualizaciones Interactivas:** Gráficos dinámicos con Plotly
- **Navegación Intuitiva:** Menú claro y accesible
- **Feedback en Tiempo Real:** Indicadores de estado y progreso
- **Documentación Integrada:** Guía completa del proyecto

## 🔧 API Endpoints

### GET /api/data_summary
Obtiene resumen estadístico del dataset

### GET /api/model_status
Verifica estado del modelo entrenado

### POST /train_models
Inicia proceso de entrenamiento de modelos

### POST /make_prediction
Realiza predicción para un job específico

## 📊 Resultados Esperados

### Impacto en el Negocio
- Reducción del 15-25% en fallos de backup
- Optimización de ventanas de backup
- Mejor distribución de carga entre servidores
- Alertas tempranas para jobs de riesgo
- Toma de decisiones basada en datos

### Rendimiento Técnico
- Tiempo de respuesta < 2 segundos
- Precisión del modelo > 85%
- Disponibilidad del sistema > 99%
- Procesamiento de 80k+ registros

## 🚀 Despliegue en Producción

### Consideraciones
- Configurar variables de entorno
- Usar servidor WSGI (Gunicorn)
- Implementar HTTPS
- Configurar logging y monitoreo
- Establecer backup de modelos

### Comandos de Despliegue
```bash
# Usando Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Con variables de entorno
export FLASK_ENV=production
export FLASK_DEBUG=False
```

## 🔄 Mantenimiento

### Actualización de Modelos
- Reentrenar cada 30 días con nuevos datos
- Monitorear degradación del rendimiento
- Validar nuevas versiones antes del despliegue

### Backup y Recuperación
- Backup automático de modelos entrenados
- Respaldo de configuraciones
- Plan de recuperación ante desastres

## 🤝 Contribuciones

### Desarrollo Futuro
- Implementación de más algoritmos ML
- Integración con APIs de backup
- Dashboard en tiempo real
- Alertas automáticas por email
- Análisis de tendencias temporales

### Mejoras Técnicas
- Optimización de rendimiento
- Caché de predicciones
- Paralelización de entrenamientos
- Interfaz móvil nativa

## 📝 Licencia

Este proyecto está desarrollado como parte del programa académico de Ingeniería en Sistemas y Computación de la Universidad Nacional de Chimborazo.

## 👥 Autor

**Lenin Lopez**
- Carrera: Ingeniería en Sistemas y Computación
- Universidad: Universidad Nacional de Chimborazo
- Año: 2026

## 📞 Soporte

Para problemas técnicos o consultas sobre el proyecto:
- Crear issue en el repositorio
- Contactar al desarrollador
- Revisar la documentación integrada

---

**Desarrollado con ❤️ usando Python, Flask y Machine Learning**
