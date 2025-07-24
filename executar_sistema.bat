@echo off
echo.
echo ========================================
echo    🐍 TNC GESTAO - SISTEMA PYTHON
echo ========================================
echo.
echo 🚀 Iniciando sistema TNC Gestao...
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERRO: Python não encontrado!
    echo    Instale Python 3.8+ antes de continuar.
    pause
    exit /b 1
)

REM Verificar se requirements estão instalados
echo 📦 Verificando dependências...
pip show PyQt6 >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Instalando dependências necessárias...
    pip install -r requirements.txt
)

echo.
echo ✅ Tudo pronto! Iniciando TNC Gestão...
echo.
echo 📍 Localização: %cd%
echo 🎯 Executando: python main.py
echo.
echo ========================================
echo.

REM Executar o sistema
python main.py

REM Verificar se houve erro
if %errorlevel% neq 0 (
    echo.
    echo ❌ Erro ao executar o sistema!
    echo    Verifique as dependências e tente novamente.
    echo.
    pause
    exit /b 1
)

echo.
echo 🏁 Sistema TNC Gestão finalizado.
echo.
pause
