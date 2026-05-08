@echo off
echo ================================================================
echo  SISTEMA DE ANALISIS Y PREDICCION DE JOBS DE BACKUP
echo  Universidad Nacional de Chimborazo
echo  Ingenieria en Sistemas y Computacion
echo ================================================================
echo.

echo Seleccione una opcion:
echo.
echo === ANÁLISIS BÁSICO ===
echo 1. Analizar backup.csv (original)
echo 2. Analizar backup1.csv (códigos numéricos)
echo.
echo === APLICACIONES WEB ===
echo 3. App demo backup.csv
echo 4. App demo backup1.csv
echo 5. App completa con ML
echo.
echo === ANÁLISIS AVANZADO ===
echo 6. ML completo backup1.csv
echo 7. Demostración completa
echo 8. Pruebas del sistema8
echo.
echo === UTILIDADES ===
echo 9. Ver estructura del proyecto
echo 10. Salir
echo.

set /p choice="Ingrese su opcion (1-10): "

if "%choice%"=="1" (
    echo.
    echo Ejecutando analisis basico de backup.csv...
    python basic_analysis.py
    pause
    goto menu
)

if "%choice%"=="2" (
    echo.
    echo Ejecutando analisis de backup1.csv...
    python analyze_backup1.py
    pause
    goto menu
)

if "%choice%"=="3" (
    echo.
    echo Iniciando aplicacion web para backup.csv...
    echo Abra su navegador en: http://localhost:5000
    python app_demo.py
    pause
    goto menu
)

if "%choice%"=="4" (
    echo.
    echo Iniciando aplicacion web para backup1.csv...
    echo Abra su navegador en: http://localhost:5000
    python app_backup1.py
    pause
    goto menu
)

if "%choice%"=="5" (
    echo.
    echo Iniciando aplicacion web completa...
    echo Nota: Requiere dependencias de ML instaladas
    echo Abra su navegador en: http://localhost:5000
    python app.py
    pause
    goto menu
)

if "%choice%"=="6" (
    echo.
    echo Ejecutando analisis ML completo de backup1.csv...
    python ml_analysis_backup1.py
    pause
    goto menu
)

if "%choice%"=="7" (
    echo.
    echo Iniciando demostracion completa...
    python demo_complete.py
    pause
    goto menu
)

if "%choice%"=="8" (
    echo.
    echo Ejecutando pruebas del sistema...
    python test_system.py
    pause
    goto menu
)

if "%choice%"=="9" (
    echo.
    echo Estructura del proyecto:
    tree /F
    pause
    goto menu
)

if "%choice%"=="10" (
    echo.
    echo Gracias por usar el sistema!
    exit
)

echo Opcion invalida. Intente de nuevo.
pause

:menu
cls
goto start

:start
goto menu
