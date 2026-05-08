@echo off
REM Script rápido para arrancar la app en Windows (cmd)
REM Ejecutar desde la carpeta Examen\backup_ml_app
if not exist .venv (python -m venv .venv)
call .venv\Scripts\activate.bat
python app_demo.py
