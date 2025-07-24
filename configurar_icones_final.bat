@echo off
echo.
echo ========================================
echo      🖼️ CONFIGURAR ÍCONES - TNC GESTÃO
echo ========================================
echo.

REM Verificar se logo existe
if not exist "logo_rnc.ico" (
    echo ❌ ERRO: logo_rnc.ico não encontrado!
    pause
    exit /b 1
)

echo ✅ Logo encontrado: logo_rnc.ico
echo.
echo 🎯 Configurando atalhos com ícone personalizado...
echo.

REM Criar atalho principal usando VBS
echo Set WshShell = CreateObject("WScript.Shell") > temp_atalho.vbs
echo Set oShellLink = WshShell.CreateShortcut("🚀 TNC Gestão.lnk") >> temp_atalho.vbs
echo oShellLink.TargetPath = WshShell.CurrentDirectory ^& "\executar_sistema.bat" >> temp_atalho.vbs
echo oShellLink.WorkingDirectory = WshShell.CurrentDirectory >> temp_atalho.vbs
echo oShellLink.IconLocation = WshShell.CurrentDirectory ^& "\logo_rnc.ico" >> temp_atalho.vbs
echo oShellLink.Description = "TNC Gestão - Sistema de Gestão de TNCs" >> temp_atalho.vbs
echo oShellLink.Save >> temp_atalho.vbs

cscript //NoLogo temp_atalho.vbs
del temp_atalho.vbs

if exist "🚀 TNC Gestão.lnk" (
    echo ✅ Atalho principal criado: "🚀 TNC Gestão.lnk"
) else (
    echo ❌ Erro ao criar atalho principal
)

REM Criar atalho para área de trabalho
echo.
echo 📋 Deseja criar atalho na Área de Trabalho? (S/N)
set /p criar_desktop=
if /i "%criar_desktop%"=="S" (
    copy "🚀 TNC Gestão.lnk" "%USERPROFILE%\Desktop\" >nul 2>&1
    if exist "%USERPROFILE%\Desktop\🚀 TNC Gestão.lnk" (
        echo ✅ Atalho copiado para Área de Trabalho
    ) else (
        echo ❌ Erro ao copiar para Área de Trabalho
    )
)

echo.
echo ========================================
echo           🎉 CONFIGURAÇÃO CONCLUÍDA!
echo ========================================
echo.
echo ✅ Atalhos disponíveis:
echo    📎 "🚀 TNC Gestão.lnk" (com ícone personalizado)
echo    📄 "executar_sistema.bat" (original)
echo.
echo 🎯 Para executar o sistema:
echo    1. Clique duplo no atalho "🚀 TNC Gestão.lnk"
echo    2. Ou execute "executar_sistema.bat"
echo.
echo 💡 DICA: O atalho .lnk pode ser movido para:
echo    - Área de Trabalho (já criado se solicitado)
echo    - Menu Iniciar
echo    - Barra de Tarefas
echo.
pause
