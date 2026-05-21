"""
Integración del Chatbot con la aplicación Flask
"""

from flask import Flask, render_template, request, jsonify
from chatbot_backup import BackupChatbot
import json

# Instancia global del chatbot
chatbot = BackupChatbot()

def init_chatbot_routes(app):
    """Inicializar rutas del chatbot en la aplicación Flask"""
    
    @app.route('/chatbot')
    def chatbot_page():
        """Página del chatbot"""
        return render_template('chatbot.html')
    
    @app.route('/api/chatbot/message', methods=['POST'])
    def chatbot_message():
        """Endpoint para enviar mensajes al chatbot"""
        try:
            data = request.get_json()
            user_message = data.get('message', '').strip()
            
            if not user_message:
                return jsonify({
                    'status': 'error',
                    'message': 'Mensaje vacío'
                })
            
            # Procesar mensaje con el chatbot
            bot_response = chatbot.handle_message(user_message)
            
            return jsonify({
                'status': 'success',
                'user_message': user_message,
                'bot_response': bot_response,
                'timestamp': chatbot.conversation_history[-1]['timestamp']
            })
            
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': f'Error procesando mensaje: {str(e)}'
            })
    
    @app.route('/api/chatbot/history')
    def chatbot_history():
        """Obtener historial de conversación"""
        try:
            return jsonify({
                'status': 'success',
                'history': chatbot.conversation_history,
                'context': chatbot.get_conversation_context()
            })
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': f'Error obteniendo historial: {str(e)}'
            })
    
    @app.route('/api/chatbot/reset', methods=['POST'])
    def chatbot_reset():
        """Reiniciar conversación del chatbot"""
        try:
            response = chatbot.reset_conversation()
            return jsonify({
                'status': 'success',
                'message': response
            })
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': f'Error reiniciando chatbot: {str(e)}'
            })
    
    @app.route('/api/chatbot/quick-actions')
    def chatbot_quick_actions():
        """Obtener acciones rápidas del chatbot"""
        quick_actions = [
            {
                'text': '📊 Estado del Sistema',
                'message': 'estado del sistema',
                'icon': 'fas fa-chart-line'
            },
            {
                'text': '🔍 Análisis de Datos',
                'message': 'análisis de tendencias',
                'icon': 'fas fa-search'
            },
            {
                'text': '🎯 Hacer Predicción',
                'message': 'predicción de riesgo',
                'icon': 'fas fa-bullseye'
            },
            {
                'text': '🚀 Optimización',
                'message': 'recomendaciones de optimización',
                'icon': 'fas fa-rocket'
            },
            {
                'text': '🛠️ Solucionar Problemas',
                'message': 'tengo problemas con mis backups',
                'icon': 'fas fa-tools'
            },
            {
                'text': '❓ Ayuda',
                'message': 'ayuda',
                'icon': 'fas fa-question-circle'
            }
        ]
        
        return jsonify({
            'status': 'success',
            'quick_actions': quick_actions
        })

# Para usar en app.py principal
def register_chatbot_routes(app):
    """Función para registrar las rutas del chatbot"""
    init_chatbot_routes(app)
