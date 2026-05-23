"""Integracion del chatbot con la aplicacion Flask."""

import os

from flask import render_template, request, jsonify
from chatbot_backup import BackupChatbot

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
            },
            {
                'text': '🧯 Status 96',
                'message': 'Tengo status 96 en un job de NetBackup en windows',
                'icon': 'fas fa-fire-extinguisher'
            },
            {
                'text': '📚 Estado entrenamiento',
                'message': 'entrenamiento pdf',
                'icon': 'fas fa-book'
            }
        ]
        
        return jsonify({
            'status': 'success',
            'quick_actions': quick_actions
        })

    @app.route('/api/chatbot/knowledge/stats')
    def chatbot_knowledge_stats():
        """Obtener estadisticas de la base de conocimiento."""
        try:
            return jsonify({
                'status': 'success',
                'stats': chatbot.get_knowledge_stats()
            })
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': f'Error obteniendo estadisticas: {str(e)}'
            })

    @app.route('/api/chatbot/knowledge/train', methods=['POST'])
    def chatbot_knowledge_train():
        """Entrenar chatbot cargando un PDF de runbooks/incidentes."""
        try:
            if 'pdf_file' not in request.files:
                return jsonify({
                    'status': 'error',
                    'message': 'No se recibio archivo PDF'
                })

            pdf_file = request.files['pdf_file']
            if not pdf_file or not pdf_file.filename:
                return jsonify({
                    'status': 'error',
                    'message': 'Archivo invalido'
                })

            file_name = pdf_file.filename
            if not file_name.lower().endswith('.pdf'):
                return jsonify({
                    'status': 'error',
                    'message': 'Solo se permiten archivos .pdf'
                })

            os.makedirs('data/uploads', exist_ok=True)
            file_path = os.path.join('data/uploads', file_name)
            pdf_file.save(file_path)

            train_result = chatbot.train_from_pdf(file_path, source_name=file_name)
            return jsonify(train_result)

        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': f'Error entrenando conocimiento: {str(e)}'
            })

# Para usar en app.py principal
def register_chatbot_routes(app):
    """Función para registrar las rutas del chatbot"""
    init_chatbot_routes(app)
