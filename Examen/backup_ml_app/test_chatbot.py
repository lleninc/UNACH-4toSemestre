#!/usr/bin/env python3
"""
Script de prueba independiente para el Chatbot de Backup
Ejecutar desde línea de comandos para probar el chatbot sin interfaz web
"""

import sys
import os

# Agregar el directorio actual al path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chatbot_backup import BackupChatbot

def main():
    """Función principal para interacción con el chatbot por consola"""
    print("🤖 " + "="*60)
    print("🤖 ARIA - AUTOMATED RESTORE & INTELLIGENCE ASSISTANT")
    print("🤖 Chatbot Inteligente Especializado en NetBackup")
    print("🤖 " + "="*60)
    print("🤖 Escribe 'salir', 'exit' o 'quit' para terminar")
    print("🤖 Escribe 'ayuda' para ver las funcionalidades de ARIA")
    print("🤖 " + "="*60)
    
    # Inicializar chatbot
    bot = BackupChatbot()
    
    # Mensaje de bienvenida
    welcome_message = ("¡Hola! Soy ARIA - Automated Restore & Intelligence Assistant. "
                      "Estoy especializada en NetBackup y puedo ayudarte con análisis de datos, "
                      "predicciones de errores, recomendaciones de optimización y solución de problemas. "
                      "¿En qué puedo asistirte hoy?")
    
    print(f"\n🤖 Bot: {welcome_message}\n")
    
    # Loop principal de conversación
    while True:
        try:
            # Leer entrada del usuario
            user_input = input("👤 Tú: ").strip()
            
            # Verificar comandos de salida
            if user_input.lower() in ['salir', 'exit', 'quit', 'adiós', 'bye']:
                farewell = bot.handle_message("adiós")
                print(f"\n🤖 ARIA: {farewell}")
                print("\n🤖 ¡Gracias por usar ARIA - tu asistente NetBackup!")
                break
            
            # Verificar entrada vacía
            if not user_input:
                print("🤖 ARIA: Por favor, escribe algo para poder ayudarte con NetBackup.")
                continue
            
            # Procesar mensaje con el chatbot
            response = bot.handle_message(user_input)
            
            # Mostrar respuesta formateada
            print(f"\n🤖 ARIA: {response}\n")
            print("-" * 60)
            
        except KeyboardInterrupt:
            print("\n\n🤖 Sesión interrumpida por el usuario.")
            print("🤖 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("🤖 Disculpa, hubo un problema. ¿Puedes intentar de nuevo?")

def demo_conversation():
    """Función para demostración automática del chatbot"""
    print("🎬 " + "="*60)
    print("🎬 DEMOSTRACIÓN AUTOMÁTICA DEL CHATBOT")
    print("🎬 " + "="*60)
    
    bot = BackupChatbot()
    
    # Conversación de demostración
    demo_messages = [
        "Hola",
        "¿Cuál es el estado del sistema?",
        "Dame un análisis de tendencias",
        "¿Puedes hacer una predicción?",
        "¿Qué recomendaciones tienes para optimizar?",
        "Tengo problemas con mis backups, ¿qué hago?",
        "Gracias, adiós"
    ]
    
    for i, message in enumerate(demo_messages, 1):
        print(f"\n{i}. 👤 Usuario: {message}")
        response = bot.handle_message(message)
        print(f"   🤖 Bot: {response}")
        print("-" * 50)
        
        # Pausa entre mensajes para mejor lectura
        input("   [Presiona Enter para continuar...]")

def test_specific_features():
    """Función para probar características específicas"""
    print("🧪 " + "="*60)
    print("🧪 PRUEBAS DE CARACTERÍSTICAS ESPECÍFICAS")
    print("🧪 " + "="*60)
    
    bot = BackupChatbot()
    
    # Pruebas específicas
    tests = [
        {
            "name": "Detección de Intenciones",
            "messages": ["estado", "analizar datos", "predecir error", "optimizar", "problema"]
        },
        {
            "name": "Respuestas Contextuales",
            "messages": ["backup", "jobs", "error", "servidor", "política"]
        },
        {
            "name": "Comandos de Ayuda",
            "messages": ["ayuda", "qué puedes hacer", "funciones"]
        }
    ]
    
    for test in tests:
        print(f"\n🧪 Probando: {test['name']}")
        print("-" * 30)
        
        for message in test['messages']:
            intent = bot.detect_intent(message)
            response = bot.handle_message(message)
            print(f"Mensaje: '{message}' -> Intención: {intent}")
            print(f"Respuesta: {response[:100]}..." if len(response) > 100 else f"Respuesta: {response}")
            print()

if __name__ == "__main__":
    print("🤖 Chatbot de Backup - Opciones de Prueba")
    print("1. Conversación interactiva")
    print("2. Demostración automática")
    print("3. Pruebas de características")
    print("4. Salir")
    
    while True:
        try:
            choice = input("\n🤖 Selecciona una opción (1-4): ").strip()
            
            if choice == "1":
                main()
                break
            elif choice == "2":
                demo_conversation()
                break
            elif choice == "3":
                test_specific_features()
                break
            elif choice == "4":
                print("🤖 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida. Por favor, selecciona 1, 2, 3 o 4.")
                
        except KeyboardInterrupt:
            print("\n\n🤖 ¡Hasta luego!")
            break
