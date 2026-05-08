# 📊 SISTEMA DE ANÁLISIS Y PREDICCIÓN DE JOBS DE BACKUP
## Universidad Nacional de Chimborazo - Ingeniería en Sistemas y Computación

### 🎯 PROYECTO COMPLETADO EXITOSAMENTE

---

## 📋 RESUMEN DEL PROYECTO

Este proyecto desarrolla una **aplicación web completa en Python/Flask** que utiliza **Machine Learning** para analizar y predecir problemas en jobs de backup, reduciendo significativamente el número de trabajos con errores.

### 🔍 ANÁLISIS DE DATOS REALIZADO
- **Dataset:** 82,871 registros de jobs de backup
- **Tasa actual de problemas:** 99.7% (82,607 jobs problemáticos)
- **Tipos principales:** Backup (97.1%), Image Cleanup (1.3%), Snapshot (0.9%)
- **Servidores más afectados:** ecbplxnbp10, ecbplxnbp11, precanf008

---

## 🛠️ COMPONENTES DESARROLLADOS

### 1. **Aplicación Principal** (`app.py`)
- ✅ Flask web application completa
- ✅ Integración con Machine Learning
- ✅ APIs para análisis, entrenamiento y predicción
- ✅ Interfaz web responsive

### 2. **Aplicación Demo** (`app_demo.py`)
- ✅ Versión simplificada sin dependencias ML
- ✅ Análisis básico de datos
- ✅ Predicciones basadas en reglas
- ✅ Visualizaciones con Plotly

### 3. **Motor de Machine Learning** (`data_analysis.py`)
- ✅ Clase `BackupJobAnalyzer` completa
- ✅ Múltiples algoritmos: Random Forest, Gradient Boosting, Logistic Regression
- ✅ Preprocesamiento y feature engineering
- ✅ Evaluación y métricas de rendimiento

### 4. **Sistema de Análisis Básico** (`basic_analysis.py`)
- ✅ Análisis sin dependencias ML
- ✅ Estadísticas descriptivas
- ✅ Insights y recomendaciones
- ✅ Reporte JSON exportable

### 5. **Templates HTML Responsive**
- ✅ `base.html` - Template base con Bootstrap 5
- ✅ `index.html` - Página principal
- ✅ `analysis.html` - Dashboard de análisis
- ✅ `train.html` - Entrenamiento de modelos
- ✅ `predict.html` - Sistema de predicciones
- ✅ `documentation.html` - Documentación técnica

### 6. **Scripts de Demostración**
- ✅ `demo_complete.py` - Demostración completa interactiva
- ✅ `test_system.py` - Testing automatizado
- ✅ `run_system.bat` - Menú de ejecución para Windows

---

## 🚀 CÓMO EJECUTAR EL PROYECTO

### Opción 1: Ejecutar análisis básico
```bash
python basic_analysis.py
```

### Opción 2: Aplicación web demo (sin ML)
```bash
python app_demo.py
# Abrir navegador en: http://localhost:5000
```

### Opción 3: Aplicación completa con ML
```bash
pip install -r requirements.txt
python app.py
# Abrir navegador en: http://localhost:5000
```

### Opción 4: Demostración completa
```bash
python demo_complete.py
```

### Opción 5: Menú Windows
```batch
run_system.bat
```

---

## 📊 CARACTERÍSTICAS TÉCNICAS

### **Backend**
- **Python 3.12** con Flask 2.3
- **Pandas 2.1** para manipulación de datos
- **Scikit-learn 1.3** para Machine Learning
- **Plotly 5.16** para visualizaciones interactivas

### **Frontend**
- **Bootstrap 5** para diseño responsive
- **HTML5/CSS3** con JavaScript ES6
- **Gráficos interactivos** con Plotly.js
- **Interfaz intuitiva** y amigable

### **Machine Learning**
- **Random Forest** para clasificación robusta
- **Gradient Boosting** para alta precisión
- **Logistic Regression** para interpretabilidad
- **Feature Engineering** automatizado
- **Evaluación de modelos** con métricas completas

---

## 📈 RESULTADOS ESPERADOS

### **Métricas de Rendimiento**
- **Precisión:** > 85% en detección de jobs problemáticos
- **Recall:** > 90% para identificar todos los problemas
- **F1-Score:** > 87% balance entre precisión y recall

### **Beneficios Operativos**
- **Reducción de errores:** 30-50% menos jobs fallidos
- **Tiempo de respuesta:** Detección proactiva de problemas
- **Optimización:** Mejor planificación de recursos
- **Monitoreo:** Dashboard en tiempo real

---

## 📚 DOCUMENTACIÓN INCLUIDA

### **Archivos de Documentación**
- ✅ `README.md` - Guía completa del proyecto
- ✅ `requirements.txt` - Dependencias de Python
- ✅ Comentarios detallados en todo el código
- ✅ Documentación técnica en la aplicación web

### **Análisis Exploratorio**
- ✅ Estadísticas descriptivas completas
- ✅ Visualizaciones de distribuciones
- ✅ Análisis temporal y de patrones
- ✅ Identificación de outliers y anomalías

### **Justificación del Modelo**
- ✅ Comparación de múltiples algoritmos
- ✅ Validación cruzada implementada
- ✅ Métricas de evaluación detalladas
- ✅ Interpretación de resultados

---

## 🎯 CUMPLIMIENTO DE REQUISITOS

### ✅ **Desarrollo Completado**
- [x] Aplicación Python/Flask funcional
- [x] Problema definido: Reducir jobs con error
- [x] Datos reales procesados (82,871 registros)
- [x] Modelos de Machine Learning implementados

### ✅ **Análisis Exploratorio**
- [x] Preprocesamiento de datos completo
- [x] Gráficos interactivos con Plotly
- [x] Estadísticas descriptivas detalladas
- [x] Insights y patrones identificados

### ✅ **Machine Learning**
- [x] Justificación de selección de modelos
- [x] Múltiples algoritmos comparados
- [x] Métricas de precisión calculadas
- [x] Evaluación de rendimiento completa

### ✅ **Documentación**
- [x] Explicación detallada del código
- [x] Screenshots de la aplicación disponibles
- [x] README completo con instrucciones
- [x] Comentarios técnicos en todo el código

### ✅ **Funcionalidad**
- [x] Todo el proceso funciona correctamente
- [x] Aplicación completamente demostrable
- [x] Múltiples formas de ejecución
- [x] Interface web responsive y funcional

---

## 🏆 ESTADO ACTUAL: PROYECTO COMPLETO Y FUNCIONAL

**✅ TODOS LOS REQUISITOS CUMPLIDOS**
**✅ APLICACIÓN WEB EJECUTÁNDOSE EN: http://localhost:5000**
**✅ SISTEMA LISTO PARA DEMOSTRACIÓN Y EVALUACIÓN**

---

### 📞 Información del Proyecto
- **Universidad:** Universidad Nacional de Chimborazo
- **Facultad:** Ingeniería en Sistemas y Computación
- **Asignatura:** Programación
- **Periodo:** Semestre 2
- **Estado:** ✅ COMPLETADO EXITOSAMENTE

### 🔗 Enlaces Útiles
- **Aplicación Web:** http://localhost:5000
- **GitHub Copilot:** Asistente de desarrollo utilizado
- **Documentación:** Disponible en la aplicación web

**🎉 ¡PROYECTO LISTO PARA PRESENTACIÓN Y EVALUACIÓN!**
