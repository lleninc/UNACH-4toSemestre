@echo off
echo =====================================================
echo  ARIA - NETBACKUP INTELLIGENCE ASSISTANT
echo  Sistema ML con Chatbot IA Integrado
echo =====================================================
echo.

:MENU
echo Selecciona una opcion:
echo 1. Ejecutar aplicacion web completa (Flask + ARIA)
echo 2. Probar ARIA en consola interactiva
echo 3. Demo automatica de ARIA
echo 4. Instalar dependencias
echo 5. Verificar estado del sistema
echo 6. Salir
echo.
set /p choice="Ingresa tu opcion (1-6): "

if "%choice%"=="1" goto WEB_APP
if "%choice%"=="2" goto CONSOLE_CHAT
if "%choice%"=="3" goto DEMO_CHAT
if "%choice%"=="4" goto INSTALL_DEPS
if "%choice%"=="5" goto CHECK_STATUS
if "%choice%"=="6" goto EXIT

echo Opcion no valida. Intenta de nuevo.
echo.
goto MENU

:WEB_APP
echo.
echo ====================================
echo  INICIANDO APLICACION WEB COMPLETA
echo ====================================
echo.
echo La aplicacion estara disponible en: http://localhost:5000
echo Para acceder a ARIA: http://localhost:5000/chatbot
echo.
echo Presiona Ctrl+C para detener el servidor
echo.
python app.py
goto MENU

:CONSOLE_CHAT
echo.
echo ====================================
echo  ARIA EN MODO CONSOLA INTERACTIVA
echo ====================================
echo.
python test_chatbot.py
goto MENU

:DEMO_CHAT
echo.
echo ====================================
echo  DEMOSTRACION AUTOMATICA DE ARIA
echo ====================================
echo.
echo Ejecutando demo automatica de ARIA...
python -c "from test_chatbot import demo_conversation; demo_conversation()"
goto MENU

:INSTALL_DEPS
echo.
echo ====================================
echo  INSTALANDO DEPENDENCIAS
echo ====================================
echo.
echo Instalando paquetes requeridos...
pip install -r requirements.txt
echo.
echo Dependencias instaladas correctamente.
pause
goto MENU

:CHECK_STATUS
echo.
echo ====================================
echo  VERIFICANDO ESTADO DEL SISTEMA
echo ====================================
echo.
echo Verificando Python...
python --version
echo.
echo Verificando pip...
pip --version
echo.
echo Verificando dependencias principales...
python -c "import flask; print('Flask:', flask.__version__)"
python -c "import pandas; print('Pandas:', pandas.__version__)"
python -c "import sklearn; print('Scikit-learn:', sklearn.__version__)"
python -c "import plotly; print('Plotly:', plotly.__version__)"
echo.
echo Verificando archivos del proyecto...
if exist "app.py" echo [OK] app.py encontrado
if exist "chatbot_backup.py" echo [OK] chatbot_backup.py encontrado
if exist "data_analysis.py" echo [OK] data_analysis.py encontrado
if exist "templates\chatbot.html" echo [OK] templates\chatbot.html encontrado
if exist "backup1.csv" echo [OK] backup1.csv encontrado
echo.
echo Estado del sistema verificado.
pause
goto MENU

:EXIT
echo.
echo ====================================
echo  GRACIAS POR USAR EL SISTEMA
echo ====================================
echo.
echo Proyecto: Sistema de Backup ML con Chatbot
echo Universidad: Nacional de Chimborazo
echo Carrera: Ingenieria en Sistemas y Computacion
echo.
pause
exit
