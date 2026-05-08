#!/usr/bin/env bash
# Script para arrancar la app en Linux/macOS
# Ejecutar desde Examen/backup_ml_app
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
python app_demo.py
