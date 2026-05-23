# 🤖 Chatbot Inteligente para Procesos de Respaldos

## 📋 Descripción

El **Chatbot de Backup** es un asistente virtual especializado en gestión y análisis de procesos de respaldo. Utiliza procesamiento de lenguaje natural y se integra con el sistema de Machine Learning para proporcionar análisis inteligente, predicciones y recomendaciones de optimización.

## 🎯 Objetivos

- **Asistencia Inteligente**: Proporcionar respuestas contextuales sobre el estado del sistema
- **Análisis Automatizado**: Generar insights y tendencias de forma conversacional
- **Predicciones Interactivas**: Facilitar la obtención de predicciones de riesgo
- **Soporte Técnico**: Ayudar en la resolución de problemas de backup
- **Optimización Guiada**: Ofrecer recomendaciones personalizadas

## 🏗️ Arquitectura

```
Chatbot de Backup
├── chatbot_backup.py       # Clase principal del chatbot
├── chatbot_routes.py       # Rutas Flask para integración web
├── templates/chatbot.html  # Interfaz web del chatbot
├── test_chatbot.py        # Script de prueba por consola
└── README_CHATBOT.md      # Esta documentación
```

## 🧠 Capacidades del Chatbot

### 1. Detección de Intenciones
El chatbot puede reconocer diferentes tipos de consultas:

- **Saludos**: "hola", "buenos días", "hi"
- **Estado del Sistema**: "estado", "resumen", "estadísticas"
- **Análisis**: "análisis", "analizar", "tendencias"
- **Predicciones**: "predecir", "predicción", "error"
- **Optimización**: "optimizar", "mejorar", "recomendar"
- **Problemas**: "problema", "falla", "error", "troubleshoot"
- **Ayuda**: "ayuda", "help", "qué puedes hacer"

### 2. Funcionalidades Principales

#### 📊 Estado del Sistema
- Total de jobs procesados
- Tasa de errores actual
- Tasa de éxito del sistema
- Métricas en tiempo real

#### 🔍 Análisis de Tendencias
- Análisis por tipo de backup
- Patrones por día de la semana
- Distribución por horarios
- Identificación de problemas recurrentes

#### 🎯 Predicciones de Riesgo
- Probabilidad de error para jobs específicos
- Clasificación de riesgo (Bajo/Medio/Alto)
- Factores que influyen en el resultado

#### 🚀 Recomendaciones de Optimización
- Mejores horarios para backup
- Identificación de servidores problemáticos
- Sugerencias de políticas
- Optimización de recursos

#### 🛠️ Solución de Problemas
- Diagnóstico automatizado
- Checklist de verificación
- Guías paso a paso
- Identificación de causas comunes

## 💬 Ejemplos de Conversación

### Consulta de Estado
```
Usuario: ¿Cuál es el estado actual del sistema?
Bot: 📊 Estado del Sistema de Backup

📈 Total de jobs: 82,873
❌ Jobs con error: 9,945
📉 Tasa de error: 12.0%
✅ Tasa de éxito: 88.0%
```

### Análisis de Tendencias
```
Usuario: Dame un análisis de tendencias
Bot: 📊 Análisis de Tendencias

Por tipo de backup:
• Backup: 8.5% error rate
• Replication: 15.2% error rate
• Snapshot: 6.8% error rate

💡 Usa 'optimización' para ver recomendaciones específicas.
```

### Predicción de Riesgo
```
Usuario: ¿Puedes hacer una predicción?
Bot: 🎯 Predicción de riesgo: Medio
📊 Probabilidad de error: 45.3%
🔮 Resultado esperado: ⚠️ Riesgo moderado

💡 Puedes proporcionar parámetros específicos para una predicción personalizada.
```

## 🔧 Uso del Chatbot

### Flujo Operativo L1.5 (NetBackup)
1. El operador revisa jobs en NetBackup.
2. Si detecta un error, ingresa al chat y comparte status code + job id.
3. El chatbot responde con runbook L1.5:
    - causas probables
    - pasos de remediacion
    - comandos sugeridos para consola NetBackup
4. El operador ejecuta y valida resultado.
5. Si aparece un caso nuevo, se entrena el chatbot con PDF del incidente resuelto.

### Entrenamiento por PDF
La pantalla del chatbot incluye un panel para cargar documentos PDF.

- Endpoint: `POST /api/chatbot/knowledge/train`
- Campo esperado: `pdf_file`
- Resultado: cantidad de paginas procesadas y fragmentos indexados

Estadisticas del conocimiento cargado:

- Endpoint: `GET /api/chatbot/knowledge/stats`
- Retorna total de fragmentos y lista de fuentes PDF

Dependencia requerida para procesar PDFs:

```bash
pip install pypdf
```

### Interfaz Web
1. Navegar a `/chatbot` en la aplicación Flask
2. Usar el área de chat interactiva
3. Aprovechar las acciones rápidas
4. Exportar conversaciones si es necesario

### Línea de Comandos
```bash
# Ejecutar prueba interactiva
python test_chatbot.py

# Opciones disponibles:
# 1. Conversación interactiva
# 2. Demostración automática
# 3. Pruebas de características
```

### Integración Programática
```python
from chatbot_backup import BackupChatbot

# Inicializar chatbot
bot = BackupChatbot()

# Enviar mensaje
response = bot.handle_message("estado del sistema")
print(response)

# Obtener contexto
context = bot.get_conversation_context()
```

## 🎨 Características de la Interfaz

### Diseño Responsivo
- Compatible con dispositivos móviles
- Interfaz adaptativa
- Navegación intuitiva

### Funcionalidades Interactivas
- Mensajes en tiempo real
- Indicador de escritura
- Acciones rápidas
- Sonidos de notificación
- Exportación de conversaciones

### Elementos Visuales
- Avatares diferenciados (usuario/bot)
- Códigos de colores para tipos de mensaje
- Iconos contextuales
- Animaciones suaves

## 🔌 Integración con el Sistema ML

El chatbot se integra directamente con:

- **BackupJobAnalyzer**: Para análisis de datos
- **Modelos ML**: Para predicciones
- **Base de datos**: Para métricas en tiempo real
- **Sistema de logging**: Para seguimiento de conversaciones

## 📊 Métricas y Monitoreo

### Seguimiento de Conversaciones
- Historial completo de mensajes
- Detección de intenciones
- Tiempo de respuesta
- Satisfacción del usuario

### Análisis de Uso
- Preguntas más frecuentes
- Patrones de interacción
- Efectividad de respuestas
- Áreas de mejora

## 🚀 Casos de Uso

### 1. Monitoreo Diario
```
"¿Cómo estuvo el sistema ayer?"
"¿Hay algún problema que deba atender?"
"Dame un resumen de la última semana"
```

### 2. Troubleshooting
```
"Tengo muchos errores en los backups de SQL"
"¿Por qué fallan los jobs de madrugada?"
"El servidor X está dando problemas"
```

### 3. Planificación
```
"¿Cuál es el mejor horario para hacer backups?"
"¿Qué políticas me recomiendas?"
"¿Cómo puedo optimizar mis ventanas de backup?"
```

### 4. Análisis Predictivo
```
"¿Este job va a fallar?"
"¿Qué probabilidad de éxito tiene mi backup?"
"¿Cuáles son los factores de riesgo?"
```

## 🔧 Personalización

### Agregar Nuevas Intenciones
```python
# En chatbot_backup.py
self.intent_patterns = {
    "nueva_intencion": [r"palabra1", r"palabra2", r"patron_regex"],
    # ... otras intenciones
}
```

### Expandir Base de Conocimiento
```python
# En chatbot_backup.py
self.knowledge_base = {
    "nueva_categoria": [
        "Respuesta 1",
        "Respuesta 2",
        "Respuesta 3"
    ],
    # ... otras categorías
}
```

### Personalizar Respuestas
```python
def handle_custom_intent(self, message):
    """Manejar intención personalizada"""
    # Lógica personalizada
    return "Respuesta personalizada"
```

## 🛡️ Consideraciones de Seguridad

- **Sanitización de Entrada**: Limpieza de mensajes del usuario
- **Control de Acceso**: Integración con sistema de autenticación
- **Logging Seguro**: Registro sin información sensible
- **Rate Limiting**: Control de frecuencia de mensajes

## 📈 Rendimiento

### Optimizaciones Implementadas
- Cache de modelos ML
- Respuestas pre-computadas
- Procesamiento asíncrono
- Límites de memoria

### Métricas de Rendimiento
- Tiempo de respuesta < 2 segundos
- Soporte para 100+ usuarios concurrentes
- Disponibilidad > 99.9%
- Precisión de intenciones > 90%

## 🔄 Mantenimiento

### Actualización de Modelos
- Reentrenamiento periódico
- Validación de nuevas versiones
- Rollback automático en caso de problemas

### Mejora Continua
- Análisis de conversaciones
- Identificación de gaps de conocimiento
- Expansión de capacidades
- Optimización de respuestas

## 🤝 Contribución

### Áreas de Desarrollo
- Nuevas intenciones y patrones
- Integración con APIs externas
- Mejoras en NLP
- Funcionalidades avanzadas

### Proceso de Contribución
1. Identificar área de mejora
2. Desarrollar funcionalidad
3. Probar exhaustivamente
4. Documentar cambios
5. Integrar con sistema principal

## 📝 Licencia y Créditos

**Desarrollado como parte del proyecto de Machine Learning para análisis de backup**
- Universidad Nacional de Chimborazo
- Carrera de Ingeniería en Sistemas y Computación
- Año: 2025

---

**🤖 "Asistiendo en el mundo de los respaldos, una conversación a la vez"**
