# Empaqueta la app backup_ml_app en un directorio listo para compartir por GitHub
# Uso: desde la raíz del repositorio ejecutar: .\package_for_share.ps1

$src = Join-Path -Path $PSScriptRoot -ChildPath "Examen\backup_ml_app"
$dst = Join-Path -Path $PSScriptRoot -ChildPath "deploy_backup_ml_app"

if (Test-Path $dst) {
    Write-Host "El directorio de destino ya existe. Se eliminará y recreará: $dst" -ForegroundColor Yellow
    Remove-Item -Recurse -Force $dst
}

Write-Host "Copiando desde: $src" -ForegroundColor Green
New-Item -ItemType Directory -Path $dst | Out-Null

# Copiar todo el contenido de la app
Copy-Item -Path (Join-Path $src '*') -Destination $dst -Recurse -Force

# Quitar caches y archivos innecesarios
Get-ChildItem -Path $dst -Recurse -Include '__pycache__' | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

# Crear README específico para la distribución
$readme = @"
Distribución de la aplicación Backup ML (app_demo)

Contenido:
- app_demo.py (app principal)
- requirements.txt (dependencias)
- data/ (CSV de ejemplo)
- templates/, static/ (plantillas y recursos)
- chatbot_backup.py, chatbot_routes.py y otros módulos auxiliares

Instrucciones rápidas para ejecutar (Windows):
1. Crear un virtualenv:
   python -m venv .venv
2. Activar el virtualenv:
   .\.venv\Scripts\Activate.ps1   (PowerShell)
3. Instalar dependencias:
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
4. Ejecutar la app:
   python app_demo.py

Si vas a subir a GitHub, sube la carpeta 'deploy_backup_ml_app' generada por este script.
"@

Set-Content -Path (Join-Path $dst 'README_DIStribucion.md') -Value $readme -Encoding UTF8

Write-Host "Empaquetado completado: $dst" -ForegroundColor Cyan
