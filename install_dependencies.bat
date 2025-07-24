@echo off
echo ========================================
echo TNC Gestao - Instalacao de Dependencias
echo ========================================
echo.

echo Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado!
    echo Instale Python 3.8 ou superior de https://python.org
    pause
    exit /b 1
)

echo.
echo Atualizando pip...
python -m pip install --upgrade pip

echo.
echo Instalando dependencias principais...
python -m pip install PyQt6

echo.
echo Instalando dependencias para PDF...
python -m pip install reportlab

echo.
echo Instalando dependencias para dados...
python -m pip install pandas matplotlib

echo.
echo Instalando dependencias adicionais...
python -m pip install pillow openpyxl

echo.
echo Verificando instalacao...
python -c "import PyQt6; print('PyQt6: OK')"
python -c "import reportlab; print('ReportLab: OK')"
python -c "import pandas; print('Pandas: OK')"
python -c "import matplotlib; print('Matplotlib: OK')"

echo.
echo ========================================
echo Instalacao concluida!
echo ========================================
echo.
echo Para testar o sistema:
echo   1. Modo console: python demo_console.py
echo   2. Interface grafica: python main.py
echo.
pause
