@echo off
echo 🎯 TNC Gestão - Executável Standalone
echo.

if not exist "dist\TNC_Gestao\TNC_Gestao.exe" (
    echo ❌ Executável não encontrado!
    echo Execute primeiro: executavel_ultra_simples.bat
    pause
    exit /b 1
)

echo 🚀 Executando TNC Gestão...
echo 📍 Local: %cd%\dist\TNC_Gestao\TNC_Gestao.exe
echo.

cd "dist\TNC_Gestao"
start TNC_Gestao.exe

echo ✅ TNC Gestão iniciado!
echo.
echo 💡 O aplicativo roda independente do Python
echo 💡 Você pode distribuir a pasta dist\TNC_Gestao completa
echo.
pause
