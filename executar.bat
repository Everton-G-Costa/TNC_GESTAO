@echo off
echo ========================================
echo TNC Gestao - Sistema de Nao Conformidades
echo ========================================
echo.

echo Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ERRO: Python nao encontrado!
    pause
    exit /b 1
)

echo.
echo Verificando dependencias...
python -c "import PyQt6; print('PyQt6: OK')" 2>nul || (echo PyQt6: FALTANDO & goto :install)
python -c "import reportlab; print('ReportLab: OK')" 2>nul || (echo ReportLab: FALTANDO & goto :install)
python -c "import pandas; print('Pandas: OK')" 2>nul || (echo Pandas: FALTANDO & goto :install)
python -c "import matplotlib; print('Matplotlib: OK')" 2>nul || (echo Matplotlib: FALTANDO & goto :install)

echo.
echo Todas as dependencias estao instaladas!
echo.

echo Testando sistema basico...
python test_basic.py
if %errorlevel% neq 0 (
    echo ERRO: Sistema basico falhou!
    pause
    exit /b 1
)

echo.
echo ========================================
echo Sistema funcionando!
echo ========================================
echo.
echo Escolha uma opcao:
echo 1. Executar interface grafica
echo 2. Demo em console
echo 3. Sair
echo.
set /p choice="Digite sua escolha (1-3): "

if "%choice%"=="1" (
    echo.
    echo Iniciando interface grafica...
    echo IMPORTANTE: Uma nova janela deve abrir!
    echo Se nao abrir, verifique se ha janelas minimizadas.
    echo.
    start python run_app.py
    echo Interface iniciada!
    goto :end
)

if "%choice%"=="2" (
    echo.
    echo Executando demo em console...
    python demo_console.py
    goto :end
)

goto :end

:install
echo.
echo Algumas dependencias estao faltando.
echo Execute: pip install PyQt6 reportlab pandas matplotlib
echo.
pause
exit /b 1

:end
echo.
echo Obrigado por usar TNC Gestao!
pause
