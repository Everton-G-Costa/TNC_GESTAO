@echo off
echo.
echo ========================================
echo    🎨 ASSOCIAR ÍCONE AOS ARQUIVOS .BAT
echo ========================================
echo.
echo ⚠️  ATENÇÃO: Esta operação modifica o registro do Windows
echo    para associar um ícone personalizado a TODOS os arquivos .bat
echo.
echo 🔧 Isso fará com que TODOS os arquivos .bat no sistema 
echo    usem o ícone do TNC Gestão.
echo.
echo 📋 Deseja continuar? (S/N)
set /p confirmar=

if /i not "%confirmar%"=="S" (
    echo ❌ Operação cancelada.
    pause
    exit /b 0
)

echo.
echo 🔧 Modificando registro do Windows...

REM Backup da configuração atual
reg export "HKEY_CLASSES_ROOT\batfile\DefaultIcon" "backup_bat_icon.reg" /y >nul 2>&1

REM Configurar novo ícone para arquivos .bat
reg add "HKEY_CLASSES_ROOT\batfile\DefaultIcon" /ve /t REG_SZ /d "%cd%\logo_rnc.ico,0" /f >nul 2>&1

if %errorlevel% equ 0 (
    echo ✅ Ícone configurado com sucesso!
    echo.
    echo 🔄 Atualizando cache de ícones...
    ie4uinit.exe -ClearIconCache >nul 2>&1
    
    echo.
    echo ✅ Configuração concluída!
    echo.
    echo 📋 Agora TODOS os arquivos .bat no sistema usarão
    echo    o ícone personalizado do TNC Gestão.
    echo.
    echo 💾 Backup criado: backup_bat_icon.reg
    echo    (para reverter, execute este arquivo)
    
) else (
    echo ❌ Erro ao configurar ícone.
    echo    Verifique se você executou como Administrador.
)

echo.
echo ========================================
echo.
pause
