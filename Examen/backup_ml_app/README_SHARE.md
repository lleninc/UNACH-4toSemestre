Distribución para compartir (instrucciones rápidas)

Objetivo: Este directorio contiene todo lo necesario para ejecutar la demo `app_demo.py` en otra máquina.

Archivos incluidos:
- `app_demo.py` — aplicación Flask principal
- `requirements.txt` — dependencias (flexibles)
- `data/backup.csv` — datos de ejemplo
- `templates/`, `static/` — recursos web
- `chatbot_backup.py`, `chatbot_routes.py` y módulos auxiliares
- `run_app.bat`, `run_app.sh` — scripts para arrancar la app

Pasos para ejecutar (Windows, desde la carpeta):

1. Crear y activar entorno virtual
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  (PowerShell) o .\.venv\Scripts\activate.bat (cmd)
2. Actualizar pip e instalar dependencias:
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
3. Ejecutar la app:
   python app_demo.py

Notas:
- No incluye el entorno virtual; se crea en la máquina destino.
- Si no quieres instalar todas las dependencias, la app puede arrancar en modo demo sin algunas funcionalidades (ver mensajes de consola).
