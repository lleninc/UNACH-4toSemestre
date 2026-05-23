"""Chatbot NetBackup L1.5 con entrenamiento incremental desde PDF."""

import json
import os
import random
import re
from datetime import datetime

from data_analysis import BackupJobAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    from pypdf import PdfReader
except Exception:
    PdfReader = None


class PDFKnowledgeBase:
    """Almacena, indexa y consulta conocimiento extraido de PDFs."""

    def __init__(self, storage_path="data/chatbot_knowledge.json"):
        self.storage_path = storage_path
        self.documents = []
        self.vectorizer = None
        self.matrix = None
        self._load()
        self._rebuild_index()

    def _load(self):
        if not os.path.exists(self.storage_path):
            self.documents = []
            return

        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                payload = json.load(f)
            self.documents = payload.get("documents", [])
        except Exception:
            self.documents = []

    def _save(self):
        os.makedirs(os.path.dirname(self.storage_path), exist_ok=True)
        payload = {
            "updated_at": datetime.now().isoformat(),
            "documents": self.documents,
        }
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

    def _rebuild_index(self):
        texts = [doc.get("text", "") for doc in self.documents if doc.get("text")]
        if not texts:
            self.vectorizer = None
            self.matrix = None
            return

        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
        self.matrix = self.vectorizer.fit_transform(texts)

    @staticmethod
    def _chunk_text(text, chunk_size=180, overlap=40):
        words = text.split()
        if not words:
            return []

        chunks = []
        step = max(1, chunk_size - overlap)
        for start in range(0, len(words), step):
            chunk_words = words[start:start + chunk_size]
            if not chunk_words:
                continue
            chunks.append(" ".join(chunk_words))
            if start + chunk_size >= len(words):
                break
        return chunks

    def add_pdf(self, pdf_path, source_name=None):
        if PdfReader is None:
            return {
                "status": "error",
                "message": "Falta dependencia 'pypdf'. Instala pypdf para entrenar desde PDF.",
            }

        if not os.path.exists(pdf_path):
            return {
                "status": "error",
                "message": f"No se encontro el archivo: {pdf_path}",
            }

        try:
            reader = PdfReader(pdf_path)
            base_name = source_name or os.path.basename(pdf_path)
            chunks_added = 0
            pages_with_text = 0

            for page_index, page in enumerate(reader.pages, start=1):
                page_text = (page.extract_text() or "").strip()
                if not page_text:
                    continue

                pages_with_text += 1
                for chunk in self._chunk_text(page_text):
                    chunks_added += 1
                    self.documents.append(
                        {
                            "id": f"{base_name}-{page_index}-{chunks_added}",
                            "source": base_name,
                            "page": page_index,
                            "added_at": datetime.now().isoformat(),
                            "text": chunk,
                        }
                    )

            self._save()
            self._rebuild_index()

            return {
                "status": "success",
                "message": "PDF procesado correctamente",
                "source": base_name,
                "pages_total": len(reader.pages),
                "pages_with_text": pages_with_text,
                "chunks_added": chunks_added,
                "documents_total": len(self.documents),
            }
        except Exception as exc:
            return {
                "status": "error",
                "message": f"Error procesando PDF: {exc}",
            }

    def search(self, query, top_k=3, min_score=0.08):
        if not query or self.vectorizer is None or self.matrix is None:
            return []

        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.matrix).flatten()
        top_indices = similarities.argsort()[::-1][:top_k]

        results = []
        for idx in top_indices:
            score = float(similarities[idx])
            if score < min_score:
                continue
            doc = self.documents[idx]
            results.append(
                {
                    "score": round(score, 4),
                    "source": doc.get("source", "desconocido"),
                    "page": doc.get("page", "?"),
                    "text": doc.get("text", ""),
                }
            )
        return results

    def stats(self):
        unique_sources = sorted({doc.get("source", "desconocido") for doc in self.documents})
        return {
            "documents_total": len(self.documents),
            "pdf_sources": unique_sources,
        }

class BackupChatbot:
    def __init__(self):
        """Inicializar chatbot L1.5 especializado en NetBackup."""
        try:
            self.analyzer = BackupJobAnalyzer()
        except Exception:
            self.analyzer = None

        self.knowledge = PDFKnowledgeBase()
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
                (
                    f"Soy {self.bot_name} y puedo ayudarte con:\n"
                    "• Diagnostico de errores por status code\n"
                    "• Pasos de remediacion L1.5\n"
                    "• Comandos/script sugeridos para ejecutar\n"
                    "• Consulta semantica sobre PDFs cargados\n"
                    "• Analisis y predicciones del sistema"
                ),
                (
                    f"{self.bot_name} - Flujo sugerido para operadores:\n"
                    "1) Compartir status code del job\n"
                    "2) Validar causa probable\n"
                    "3) Ejecutar comandos guiados\n"
                    "4) Confirmar resultado y cerrar incidente"
                ),
            ]
        }

        self.error_runbooks = {
            "96": {
                "title": "Unable to allocate new media for backup",
                "causes": [
                    "Pool o storage unit sin medios disponibles",
                    "Volumenes en estado FULL/FROZEN o expiracion no liberada",
                    "Drive/path DOWN",
                ],
                "steps": [
                    "Validar estado de pools y volumenes asignados a la politica",
                    "Revisar storage unit y conectividad con media server",
                    "Liberar/reciclar medios segun politica de retencion",
                    "Reintentar job y confirmar asignacion de cinta/disco",
                ],
                "commands_windows": [
                    "bpmedialist -m <MEDIA_ID>",
                    "vmquery -a",
                    "nbstlutil report",
                ],
                "commands_unix": [
                    "bpmedialist -m <MEDIA_ID>",
                    "vmquery -a",
                    "nbstlutil report",
                ],
            },
            "84": {
                "title": "Media write error",
                "causes": [
                    "Problema fisico de dispositivo o cinta",
                    "Timeout o caida de conectividad con storage",
                    "Path de escritura degradado",
                ],
                "steps": [
                    "Correlacionar hora del fallo con alertas de hardware",
                    "Validar estado de drive/path y eventos SCSI/SAN",
                    "Mover job a otro recurso si aplica",
                    "Marcar media sospechosa para analisis",
                ],
                "commands_windows": [
                    "bpdbjobs -report -most_columns",
                    "bpdm -status",
                    "bperror -backstat -hoursago 4",
                ],
                "commands_unix": [
                    "bpdbjobs -report -most_columns",
                    "bpdm -status",
                    "bperror -backstat -hoursago 4",
                ],
            },
            "13": {
                "title": "File read failed",
                "causes": [
                    "Archivo bloqueado o permisos insuficientes",
                    "Sistema de archivos con errores",
                    "Ruta no accesible temporalmente",
                ],
                "steps": [
                    "Confirmar permisos del cliente y cuenta de backup",
                    "Revisar archivos bloqueados y antivirus",
                    "Validar path en la politica y retry del job",
                ],
                "commands_windows": [
                    "bperror -backstat -hoursago 2",
                    "bpdbjobs -jobid <JOB_ID> -all_columns",
                    "bpclntcmd -pn",
                ],
                "commands_unix": [
                    "bperror -backstat -hoursago 2",
                    "bpdbjobs -jobid <JOB_ID> -all_columns",
                    "bpclntcmd -pn",
                ],
            },
            "58": {
                "title": "Can't connect to client",
                "causes": [
                    "Resolucion DNS/hosts incorrecta",
                    "Puertos NetBackup bloqueados",
                    "Servicios de cliente detenidos",
                ],
                "steps": [
                    "Validar resolucion de nombre ida y vuelta",
                    "Probar conectividad de puertos 1556/13724",
                    "Confirmar estado de servicios pbx/bpcd/vnetd",
                ],
                "commands_windows": [
                    "bpclntcmd -hn <CLIENTE>",
                    "bpclntcmd -pn",
                    "bptestbpcd -client <CLIENTE> -verbose",
                ],
                "commands_unix": [
                    "bpclntcmd -hn <CLIENTE>",
                    "bpclntcmd -pn",
                    "bptestbpcd -client <CLIENTE> -verbose",
                ],
            },
            "59": {
                "title": "Access to the client was not allowed",
                "causes": [
                    "Certificados/host ID no alineados",
                    "Politica de seguridad impide acceso",
                    "Configuracion cliente-servidor inconsistente",
                ],
                "steps": [
                    "Validar certificados y trust en ambos lados",
                    "Revisar autorizaciones del cliente en el master",
                    "Confirmar que nombre del cliente coincide en politica",
                ],
                "commands_windows": [
                    "nbcertcmd -listAllCertificates",
                    "bpclntcmd -self",
                    "bptestbpcd -client <CLIENTE> -verbose",
                ],
                "commands_unix": [
                    "nbcertcmd -listAllCertificates",
                    "bpclntcmd -self",
                    "bptestbpcd -client <CLIENTE> -verbose",
                ],
            },
            "83": {
                "title": "Media open error",
                "causes": [
                    "Media no disponible o en estado incorrecto",
                    "Drive con bloqueo/logica de reserva",
                    "Inconsistencia catalogo-media",
                ],
                "steps": [
                    "Verificar disponibilidad real del media ID",
                    "Revisar locks y estado de drive",
                    "Relanzar job en ventana controlada",
                ],
                "commands_windows": [
                    "bpmedialist -l",
                    "vmoprcmd -d",
                    "bperror -backstat -hoursago 2",
                ],
                "commands_unix": [
                    "bpmedialist -l",
                    "vmoprcmd -d",
                    "bperror -backstat -hoursago 2",
                ],
            },
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
            "problemas": [r"problema", r"falla", r"error", r"issue", r"troubleshoot"],
            "entrenamiento": [r"entrena", r"pdf", r"document", r"base de conocimiento"],
        }

    @staticmethod
    def detect_error_code(message):
        patterns = [
            r"status\s*[:#-]?\s*(\d{1,3})",
            r"error\s*[:#-]?\s*(\d{1,3})",
            r"codigo\s*[:#-]?\s*(\d{1,3})",
            r"\b(\d{2,3})\b",
        ]

        message_lower = message.lower()
        for pattern in patterns:
            match = re.search(pattern, message_lower)
            if match:
                return match.group(1)
        return None

    @staticmethod
    def _detect_platform_preference(message):
        msg = message.lower()
        if any(token in msg for token in ["windows", "powershell", "cmd"]):
            return "windows"
        if any(token in msg for token in ["linux", "unix", "rhel", "aix"]):
            return "unix"
        return "windows"

    def _format_runbook(self, code, platform="windows"):
        runbook = self.error_runbooks.get(str(code))
        if not runbook:
            return None

        command_key = "commands_windows" if platform == "windows" else "commands_unix"
        commands = runbook.get(command_key, [])

        lines = [
            f"🧯 **Runbook NetBackup - Status {code}**",
            f"**Descripcion:** {runbook['title']}",
            "",
            "**Causas probables:**",
        ]

        for item in runbook.get("causes", []):
            lines.append(f"• {item}")

        lines.append("")
        lines.append("**Pasos sugeridos L1.5:**")
        for idx, step in enumerate(runbook.get("steps", []), start=1):
            lines.append(f"{idx}. {step}")

        lines.append("")
        lines.append(f"**Comandos sugeridos ({platform}):**")
        for cmd in commands:
            lines.append(f"• `{cmd}`")

        lines.append("")
        lines.append("⚠️ Ejecuta comandos en consola NetBackup con permisos adecuados y valida impacto antes de cambios permanentes.")
        return "\n".join(lines)

    def train_from_pdf(self, pdf_path, source_name=None):
        return self.knowledge.add_pdf(pdf_path, source_name=source_name)

    def get_knowledge_stats(self):
        return self.knowledge.stats()
        
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
            if self.analyzer is None:
                return {"error": "Analizador ML no disponible en este entorno."}

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
            if self.analyzer is None:
                return {"error": "Analizador ML no disponible en este entorno."}

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
            if self.analyzer is None:
                return "❌ Analizador ML no disponible en este entorno."

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
        error_code = self.detect_error_code(message)
        platform = self._detect_platform_preference(message)
        
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
            
        elif intent == "entrenamiento":
            stats = self.get_knowledge_stats()
            response = (
                "📚 **Entrenamiento por documentos**\n\n"
                "Carga PDFs usando el panel de entrenamiento en la pantalla del chatbot.\n"
                f"Actualmente hay {stats['documents_total']} fragmentos indexados de {len(stats['pdf_sources'])} PDF(s)."
            )

        elif intent == "problemas":
            if error_code and error_code in self.error_runbooks:
                response = self._format_runbook(error_code, platform=platform)
            else:
                doc_hits = self.knowledge.search(message, top_k=3)
                if doc_hits:
                    response = "🛠️ **Diagnostico con base documental**\n\n"
                    response += "No detecte un status code conocido, pero encontre guias cercanas en tus PDFs:\n"
                    for hit in doc_hits:
                        response += (
                            f"\n• Fuente: {hit['source']} (pag. {hit['page']}, score {hit['score']})\n"
                            f"  {hit['text'][:260]}..."
                        )
                    response += "\n\nComparte el status code exacto para darte comandos puntuales de remediacion."
                else:
                    response = (
                        "🛠️ **Solución de Problemas**\n\n"
                        "Para ayudarte mejor, comparte:\n"
                        "• Status code (por ejemplo 96, 84, 13, 58, 59, 83)\n"
                        "• Job ID\n"
                        "• Cliente y media server\n"
                        "• Plataforma (Windows/Linux)\n\n"
                        "Mientras tanto, validaciones iniciales:\n"
                        "✅ Espacio disponible\n"
                        "✅ Conectividad y DNS\n"
                        "✅ Estado de servicios NetBackup\n"
                        "✅ Storage Unit y politicas"
                    )

        elif error_code and error_code in self.error_runbooks:
            response = self._format_runbook(error_code, platform=platform)
            
        else:
            doc_hits = self.knowledge.search(message, top_k=3)
            if doc_hits:
                response = "📘 **Respuesta basada en documentacion cargada**\n"
                response += "\nResumen de hallazgos relevantes:\n"
                for idx, hit in enumerate(doc_hits, start=1):
                    response += (
                        f"\n{idx}. Fuente: {hit['source']} (pag. {hit['page']}, score {hit['score']})\n"
                        f"{hit['text'][:280]}...\n"
                    )
                response += (
                    "\nSi compartes status code y Job ID, te devuelvo una secuencia de comandos exacta para soporte L1.5."
                )
            else:
                response = (
                    "🤖 Puedo ayudarte con:\n\n"
                    "📊 'estado' - Ver estadisticas del sistema\n"
                    "🔍 'analisis' - Analizar tendencias\n"
                    "🎯 'prediccion' - Predecir riesgos\n"
                    "🛠️ 'status 96' (u otro codigo) - Runbook con comandos\n"
                    "📚 'entrenamiento pdf' - Estado de base documental\n\n"
                    "Comparte tu error de NetBackup y te guio paso a paso."
                )
        
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
