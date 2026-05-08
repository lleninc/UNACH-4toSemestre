"""
Chatbot Inteligente para Procesos de Respaldos
Autor: Sistema de Análisis de Backup ML
Descripción: Asistente virtual especializado en gestión y análisis de trabajos de backup

Funcionalidades:
- Responde preguntas sobre estado de respaldos
- Proporciona predicciones y análisis
- Ofrece recomendaciones de optimización
- Guía en el uso del sistema ML
"""

import re
import json
import random
from datetime import datetime
from data_analysis import BackupJobAnalyzer
import pandas as pd

class BackupChatbot:
    def __init__(self):
        """Inicializar el chatbot con conocimiento especializado en backup"""
        self.analyzer = BackupJobAnalyzer()
        self.conversation_history = []
        self.user_context = {}
        
        # Base de conocimiento especializada
        self.bot_name = "ARIA"
        self.bot_full_name = "ARIA (Automated Restore & Intelligence Assistant)"
        
        self.knowledge_base = {
            "saludos": [
                f"¡Hola! Soy {self.bot_name}, tu asistente especializado en NetBackup. ¿En qué puedo ayudarte hoy?",
                f"¡Bienvenido! Soy {self.bot_name} - Automated Restore & Intelligence Assistant. ¿Qué necesitas saber sobre tus respaldos?",
                f"¡Hola! Soy {self.bot_name}, estoy aquí para optimizar y monitorear tus procesos NetBackup. ¿Cómo puedo asistirte?"
            ],
            "despedidas": [
                f"¡Hasta luego! Recuerda que {self.bot_name} está aquí 24/7 para tus necesidades NetBackup.",
                f"¡Nos vemos! Que tengas un excelente día gestionando tus respaldos. - {self.bot_name}",
                f"¡Adiós! {self.bot_name} siempre está disponible para consultas sobre NetBackup."
            ],
            "ayuda_general": [
                f"Soy {self.bot_name} y puedo ayudarte con:\n• Análisis de estado NetBackup\n• Predicciones de errores\n• Recomendaciones de optimización\n• Estadísticas del sistema\n• Interpretación de métricas",
                f"{self.bot_name} - Mis especialidades incluyen:\n• Monitoreo de jobs NetBackup\n• Detección de patrones de error\n• Análisis de rendimiento\n• Optimización de horarios\n• Gestión de políticas"
            ]
        }
        
        # Patrones de reconocimiento de intenciones
        self.intent_patterns = {
            "saludo": [r"hola", r"buenos días", r"buenas tardes", r"saludos", r"hi"],
            "despedida": [r"adiós", r"hasta luego", r"nos vemos", r"bye", r"chao"],
            "ayuda": [r"ayuda", r"help", r"qué puedes hacer", r"funciones", r"opciones"],
            "estado_sistema": [r"estado", r"resumen", r"estadísticas", r"métricas", r"dashboard"],
            "prediccion": [r"predecir", r"predicción", r"pronóstico", r"error", r"fallo"],
            "analisis": [r"análisis", r"analizar", r"datos", r"información", r"tendencias"],
            "optimizacion": [r"optimizar", r"mejorar", r"recomendar", r"sugerir", r"optimización"],
            "problemas": [r"problema", r"falla", r"error", r"issue", r"troubleshoot"]
        }
        
    def detect_intent(self, message):
        """Detectar la intención del usuario basada en patrones"""
        message_lower = message.lower()
        
        for intent, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if re.search(pattern, message_lower):
                    return intent
        
        return "general"
    
    def get_system_status(self):
        """Obtener estado actual del sistema"""
        try:
            if self.analyzer.df is None:
                self.analyzer.load_data()
            
            total_jobs = len(self.analyzer.df)
            errors = self.analyzer.df['has_error'].sum()
            error_rate = (errors / total_jobs) * 100 if total_jobs > 0 else 0
            
            return {
                "total_jobs": total_jobs,
                "total_errors": errors,
                "error_rate": round(error_rate, 2),
                "success_rate": round(100 - error_rate, 2)
            }
        except Exception as e:
            return {"error": str(e)}
    
    def analyze_backup_trends(self):
        """Analizar tendencias de backup"""
        try:
            if self.analyzer.df is None:
                self.analyzer.load_data()
            
            # Análisis por tipo de trabajo
            type_analysis = self.analyzer.df.groupby('Type')['has_error'].agg(['count', 'sum', 'mean']).round(3)
            
            # Análisis por día de la semana
            day_analysis = self.analyzer.df.groupby('start_day_of_week')['has_error'].mean().round(3)
            
            # Análisis por hora
            hour_analysis = self.analyzer.df.groupby('start_hour')['has_error'].mean().round(3)
            
            return {
                "by_type": type_analysis.to_dict(),
                "by_day": day_analysis.to_dict(),
                "by_hour": hour_analysis.to_dict()
            }
        except Exception as e:
            return {"error": str(e)}
    
    def get_optimization_recommendations(self):
        """Generar recomendaciones de optimización"""
        try:
            status = self.get_system_status()
            trends = self.analyze_backup_trends()
            
            recommendations = []
            
            # Recomendación basada en tasa de errores
            if status.get("error_rate", 0) > 10:
                recommendations.append(
                    f"⚠️ Alta tasa de errores ({status['error_rate']}%). "
                    "Considera revisar las políticas de backup y capacidad del servidor."
                )
            elif status.get("error_rate", 0) < 5:
                recommendations.append(
                    f"✅ Excelente tasa de éxito ({status['success_rate']}%). "
                    "El sistema está funcionando óptimamente."
                )
            
            # Recomendaciones por horario
            if "by_hour" in trends and trends["by_hour"]:
                worst_hour = max(trends["by_hour"], key=trends["by_hour"].get)
                best_hour = min(trends["by_hour"], key=trends["by_hour"].get)
                
                recommendations.append(
                    f"🕐 Hora con más errores: {worst_hour}:00 "
                    f"({trends['by_hour'][worst_hour]*100:.1f}% error rate)"
                )
                recommendations.append(
                    f"🕐 Mejor hora para backups: {best_hour}:00 "
                    f"({trends['by_hour'][best_hour]*100:.1f}% error rate)"
                )
            
            # Recomendaciones por tipo
            if "by_type" in trends and trends["by_type"]:
                for backup_type, stats in trends["by_type"]["mean"].items():
                    if stats > 0.15:  # 15% error rate
                        recommendations.append(
                            f"⚠️ Tipo '{backup_type}' tiene alta tasa de errores ({stats*100:.1f}%)"
                        )
            
            return recommendations
            
        except Exception as e:
            return [f"Error generando recomendaciones: {str(e)}"]
    
    def predict_job_risk(self, job_params=None):
        """Predecir riesgo de error para un job"""
        try:
            if self.analyzer.model is None:
                model_loaded = self.analyzer.load_model()
                if not model_loaded:
                    return "❌ Modelo no disponible. Necesitas entrenar el modelo primero."
            
            if job_params is None:
                # Usar parámetros por defecto para demo
                job_params = {
                    'Type': 'Backup',
                    'Job Policy': 'Standard',
                    'Media Server': 'Server01',
                    'Job Schedule': 'Daily',
                    'start_hour': 23,
                    'start_day_of_week': 1,
                    'kb_sec_numeric': 1000,
                    'kilobytes_numeric': 1000000,
                    'speed_category': 'Medium',
                    'size_category': 'Medium'
                }
            
            prediction = self.analyzer.predict_job_error(job_params)
            
            risk_level = "Bajo" if prediction['probability'] < 0.3 else "Medio" if prediction['probability'] < 0.7 else "Alto"
            
            return (f"🎯 Predicción de riesgo: {risk_level}\n"
                   f"📊 Probabilidad de error: {prediction['probability']*100:.1f}%\n"
                   f"🔮 Resultado esperado: {'❌ Error probable' if prediction['prediction'] else '✅ Éxito probable'}")
            
        except Exception as e:
            return f"Error en predicción: {str(e)}"
    
    def handle_message(self, message):
        """Manejar mensaje del usuario y generar respuesta"""
        # Detectar intención
        intent = self.detect_intent(message)
        
        # Guardar en historial
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "user_message": message,
            "detected_intent": intent
        })
        
        # Generar respuesta basada en intención
        if intent == "saludo":
            response = random.choice(self.knowledge_base["saludos"])
            
        elif intent == "despedida":
            response = random.choice(self.knowledge_base["despedidas"])
            
        elif intent == "ayuda":
            response = random.choice(self.knowledge_base["ayuda_general"])
            
        elif intent == "estado_sistema":
            status = self.get_system_status()
            if "error" in status:
                response = f"❌ Error obteniendo estado: {status['error']}"
            else:
                response = (f"📊 **Estado del Sistema de Backup**\n\n"
                           f"📈 Total de jobs: {status['total_jobs']:,}\n"
                           f"❌ Jobs con error: {status['total_errors']:,}\n"
                           f"📉 Tasa de error: {status['error_rate']}%\n"
                           f"✅ Tasa de éxito: {status['success_rate']}%")
            
        elif intent == "analisis":
            trends = self.analyze_backup_trends()
            if "error" in trends:
                response = f"❌ Error en análisis: {trends['error']}"
            else:
                response = "📊 **Análisis de Tendencias**\n\n"
                if "by_type" in trends:
                    response += "**Por tipo de backup:**\n"
                    for backup_type, error_rate in trends["by_type"]["mean"].items():
                        response += f"• {backup_type}: {error_rate*100:.1f}% error rate\n"
                response += "\n💡 Usa 'optimización' para ver recomendaciones específicas."
            
        elif intent == "optimizacion":
            recommendations = self.get_optimization_recommendations()
            response = "🚀 **Recomendaciones de Optimización**\n\n"
            for i, rec in enumerate(recommendations, 1):
                response += f"{i}. {rec}\n\n"
            
        elif intent == "prediccion":
            response = "🔮 **Predicción de Riesgo**\n\n" + self.predict_job_risk()
            response += "\n\n💡 Puedes proporcionar parámetros específicos para una predicción personalizada."
            
        elif intent == "problemas":
            response = ("🛠️ **Solución de Problemas**\n\n"
                       "Para ayudarte mejor, dime:\n"
                       "• ¿Qué tipo de error estás experimentando?\n"
                       "• ¿En qué horario ocurre?\n"
                       "• ¿Qué tipo de backup es?\n\n"
                       "Mientras tanto, aquí tienes algunas verificaciones básicas:\n"
                       "✅ Espacio disponible en disco\n"
                       "✅ Conectividad de red\n"
                       "✅ Estado del servidor de medios\n"
                       "✅ Políticas de backup configuradas")
            
        else:
            # Respuesta general con contexto
            response = ("🤖 No estoy seguro de entender exactamente. Puedo ayudarte con:\n\n"
                       "📊 'estado' - Ver estadísticas del sistema\n"
                       "🔍 'análisis' - Analizar tendencias\n"
                       "🎯 'predicción' - Predecir riesgos\n"
                       "🚀 'optimización' - Recomendaciones\n"
                       "🛠️ 'problemas' - Solucionar errores\n\n"
                       "¿Qué te gustaría explorar?")
        
        # Guardar respuesta en historial
        self.conversation_history[-1]["bot_response"] = response
        
        return response
    
    def get_conversation_context(self):
        """Obtener contexto de la conversación"""
        return {
            "total_messages": len(self.conversation_history),
            "recent_intents": [msg["detected_intent"] for msg in self.conversation_history[-5:]],
            "user_context": self.user_context
        }
    
    def reset_conversation(self):
        """Reiniciar conversación"""
        self.conversation_history = []
        self.user_context = {}
        return "🔄 Conversación reiniciada. ¡Hola de nuevo!"

# Función de prueba
def test_chatbot():
    """Función de prueba del chatbot"""
    print("🤖 Chatbot de Backup - Modo de Prueba")
    print("=" * 50)
    
    bot = BackupChatbot()
    
    # Mensajes de prueba
    test_messages = [
        "Hola",
        "¿Cuál es el estado del sistema?",
        "Dame un análisis de tendencias",
        "¿Puedes hacer una predicción?",
        "Dame recomendaciones de optimización",
        "Tengo problemas con mis backups",
        "Adiós"
    ]
    
    for message in test_messages:
        print(f"\n👤 Usuario: {message}")
        response = bot.handle_message(message)
        print(f"🤖 Bot: {response}")
        print("-" * 30)

if __name__ == "__main__":
    test_chatbot()
