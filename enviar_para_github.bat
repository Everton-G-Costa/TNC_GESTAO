@echo off
echo ========================================
echo    PUSH FINAL PARA GITHUB - GIT COMPLETO
echo ========================================

cd /d "d:\tnc-gestao"

set GIT_EXE="C:\Program Files\Git\bin\git.exe"

echo Verificando Git...
%GIT_EXE% --version
if %errorlevel% neq 0 (
    echo ❌ Git nao encontrado em: %GIT_EXE%
    echo Tentando caminho alternativo...
    set GIT_EXE="C:\Program Files (x86)\Git\bin\git.exe"
    %GIT_EXE% --version
    if %errorlevel% neq 0 (
        echo ❌ Git nao encontrado! Instale Git for Windows
        pause
        exit /b 1
    )
)
echo ✅ Git encontrado!
echo.

echo Configurando repositorio remoto...
%GIT_EXE% remote remove origin 2>nul
%GIT_EXE% remote add origin https://github.com/Everton-G-Costa/TNC_GESTAO.git

echo.
echo Verificando configuracao...
%GIT_EXE% remote -v

echo.
echo Verificando status...
%GIT_EXE% status

echo.
echo Configurando branch main...
%GIT_EXE% branch -M main

echo.
echo FAZENDO PUSH PARA GITHUB...
echo URL: https://github.com/Everton-G-Costa/TNC_GESTAO.git
echo.

%GIT_EXE% push -u origin main

echo.
echo ========================================
echo          RESULTADO
echo ========================================

if %errorlevel% equ 0 (
    echo ✅ SUCESSO! Projeto enviado para GitHub!
    echo 🌐 URL: https://github.com/Everton-G-Costa/TNC_GESTAO
    echo 📦 Sistema TNC Gestao publicado
    echo 🎉 Pronto para a comunidade!
) else (
    echo ❌ Erro no push
    echo.
    echo Possiveis causas:
    echo 1. Necessaria autenticacao GitHub
    echo 2. Repositorio nao existe
    echo 3. Sem permissoes de escrita
    echo.
    echo Solucoes:
    echo 1. Use GitHub Desktop: https://desktop.github.com/
    echo 2. Configure credenciais Git
    echo 3. Verifique se repositorio existe
)

echo.
pause

echo ✅ Git encontrado!
echo.

REM Verificar se já é um repositório Git
if exist ".git" (
    echo 📁 Repositório Git já existe.
    echo.
    echo 📋 Comandos para enviar para GitHub:
    echo.
    echo git add .
    echo git commit -m "Sistema TNC Gestão completo e funcional"
    echo git branch -M main
    echo git remote add origin https://github.com/SEU_USUARIO/tnc-gestao.git
    echo git push -u origin main
    echo.
    echo ⚠️  Substitua SEU_USUARIO pelo seu nome de usuário do GitHub
    echo.
    goto :comandos
)

echo 🔧 Inicializando repositório Git...
echo.

REM Inicializar repositório
git init

REM Configurar usuário (se necessário)
git config --global user.name >nul 2>&1
if %errorlevel% neq 0 (
    set /p git_name=📝 Digite seu nome para Git: 
    git config --global user.name "!git_name!"
)

git config --global user.email >nul 2>&1
if %errorlevel% neq 0 (
    set /p git_email=📧 Digite seu email para Git: 
    git config --global user.email "!git_email!"
)

REM Adicionar arquivos
echo 📦 Adicionando arquivos...
git add .

REM Fazer commit inicial
echo 💾 Fazendo commit inicial...
git commit -m "Sistema TNC Gestão - Versão Python funcional completa"

REM Configurar branch principal
git branch -M main

echo.
echo ✅ Repositório Git configurado com sucesso!
echo.

:comandos
echo ========================================
echo       🚀 PRÓXIMOS PASSOS NO GITHUB
echo ========================================
echo.
echo 1. 🌐 Vá para: https://github.com
echo 2. 🔑 Faça login na sua conta
echo 3. ➕ Clique em "New repository"
echo 4. 📝 Nome sugerido: "tnc-gestao"
echo 5. 📄 Descrição: "Sistema de Gestão de TNCs em Python com PyQt6"
echo 6. ✅ Marque como "Public" ou "Private"
echo 7. ❌ NÃO inicialize com README (já temos)
echo 8. 🎯 Clique "Create repository"
echo.
echo 💻 Depois execute estes comandos:
echo.
echo git remote add origin https://github.com/SEU_USUARIO/tnc-gestao.git
echo git push -u origin main
echo.
echo ⚠️  Substitua SEU_USUARIO pelo seu nome de usuário do GitHub!
echo.
echo ========================================
echo.
pause
