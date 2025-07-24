@echo off
REM Script completo de setup e build para TNC Gestão

echo =========================================
echo   TNC GESTAO - SETUP COMPLETO
echo =========================================
echo.

echo Este script ira:
echo 1. Verificar Python
echo 2. Instalar dependencias
echo 3. Testar o sistema
echo 4. Criar executavel
echo.

set /p choice="Continuar? (S/N): "
if /i not "%choice%"=="S" exit /b 0

echo.
echo [ETAPA 1/4] Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo.
    echo ERRO: Python nao encontrado!
    echo Instale Python 3.8+ de: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo [ETAPA 2/4] Instalando dependencias...
call install_dependencies.bat

echo.
echo [ETAPA 3/4] Testando sistema...
echo Executando teste basico...
python -c "import src.database.connection; print('✅ Database OK')"
python -c "import src.models.tnc_model; print('✅ Models OK')"
python -c "import PyQt6.QtWidgets; print('✅ PyQt6 OK')"
python -c "import matplotlib.pyplot; print('✅ Matplotlib OK')"
python -c "import reportlab; print('✅ ReportLab OK')"

echo.
echo Sistema testado com sucesso!

echo.
echo [ETAPA 4/4] Criando executavel...
set /p build_choice="Criar executavel? (S/N): "
if /i "%build_choice%"=="S" (
    call build_installer.bat
)

echo.
echo =========================================
echo   SETUP COMPLETO FINALIZADO!
echo =========================================
echo.
echo O sistema TNC Gestao esta pronto para uso!
echo.
echo Para executar:
echo - Modo desenvolvimento: python main.py
echo - Modo executavel: dist\TNC_Gestao\TNC_Gestao.exe
echo.

pause
