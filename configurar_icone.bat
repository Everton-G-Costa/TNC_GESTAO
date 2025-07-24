@echo off
echo.
echo ========================================
echo   🖼️  CONFIGURAR ICONE DOS SCRIPTS
echo ========================================
echo.
echo 🎯 Configurando ícone personalizado para os scripts .bat
echo.

REM Verificar se logo existe
if not exist "logo_rnc.ico" (
    echo ❌ ERRO: logo_rnc.ico não encontrado!
    echo    Certifique-se que o arquivo logo_rnc.ico está na pasta.
    pause
    exit /b 1
)

echo ✅ Logo encontrado: logo_rnc.ico
echo.

echo 📋 Criando scripts com ícone personalizado...

REM Criar atalho para executar_sistema.bat
echo 🔧 Criando atalho: "TNC Gestão.lnk"
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('TNC Gestão.lnk'); $Shortcut.TargetPath = '%cd%\executar_sistema.bat'; $Shortcut.WorkingDirectory = '%cd%'; $Shortcut.IconLocation = '%cd%\logo_rnc.ico'; $Shortcut.Description = 'TNC Gestão - Sistema de Gestão de TNCs'; $Shortcut.Save()"

if exist "TNC Gestão.lnk" (
    echo ✅ Atalho criado: "TNC Gestão.lnk"
) else (
    echo ❌ Erro ao criar atalho principal
)

REM Criar atalho adicional para executar_tnc.bat
echo 🔧 Criando atalho alternativo: "TNC Gestão (Alternativo).lnk"
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('TNC Gestão (Alternativo).lnk'); $Shortcut.TargetPath = '%cd%\executar_tnc.bat'; $Shortcut.WorkingDirectory = '%cd%'; $Shortcut.IconLocation = '%cd%\logo_rnc.ico'; $Shortcut.Description = 'TNC Gestão - Sistema Alternativo'; $Shortcut.Save()"

if exist "TNC Gestão (Alternativo).lnk" (
    echo ✅ Atalho alternativo criado: "TNC Gestão (Alternativo).lnk"
) else (
    echo ❌ Erro ao criar atalho alternativo
)

echo.
echo ========================================
echo           🎉 CONFIGURAÇÃO CONCLUÍDA!
echo ========================================
echo.
echo ✅ Atalhos criados com ícone personalizado:
echo    📎 "TNC Gestão.lnk"
echo    📎 "TNC Gestão (Alternativo).lnk"
echo.
echo 🎯 Agora você pode:
echo    1. Usar os atalhos .lnk (com ícone)
echo    2. Ou continuar usando os .bat normais
echo.
echo 💡 DICA: Você pode mover os atalhos .lnk para:
echo    - Área de Trabalho
echo    - Menu Iniciar
echo    - Barra de Tarefas
echo.
pause
