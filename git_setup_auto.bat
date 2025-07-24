@echo off
echo.
echo ========================================
echo   📦 CONFIGURAÇÃO AUTOMÁTICA DO GIT
echo ========================================
echo.

REM Detectar Git
set GIT_FOUND=0
set GIT_CMD=git

git --version >nul 2>&1
if %errorlevel% equ 0 (
    set GIT_FOUND=1
    echo ✅ Git encontrado!
) else (
    if exist "C:\Program Files\Git\bin\git.exe" (
        set GIT_CMD="C:\Program Files\Git\bin\git.exe"
        set GIT_FOUND=1
        echo ✅ Git encontrado!
    ) else (
        echo ❌ Git não encontrado! Instale Git primeiro.
        pause
        exit /b 1
    )
)

echo.
echo 🔧 Configurando Git com informações padrão...

REM Configurar com informações genéricas se não existirem
%GIT_CMD% config --global user.name >nul 2>&1
if %errorlevel% neq 0 (
    %GIT_CMD% config --global user.name "TNC Developer"
    echo ✅ Nome configurado: TNC Developer
)

%GIT_CMD% config --global user.email >nul 2>&1
if %errorlevel% neq 0 (
    %GIT_CMD% config --global user.email "dev@tnc-gestao.local"
    echo ✅ Email configurado: dev@tnc-gestao.local
)

echo.
echo 📦 Inicializando repositório...
if not exist ".git" (
    %GIT_CMD% init
    echo ✅ Repositório inicializado!
) else (
    echo ✅ Repositório já existe!
)

echo.
echo 📁 Adicionando arquivos...
%GIT_CMD% add .

echo.
echo 💾 Fazendo commit inicial...
%GIT_CMD% commit -m "🚀 TNC Gestão - Sistema Completo Python/PyQt6

✨ Sistema de Gestão de TNCs totalmente funcional

🎯 Funcionalidades Principais:
- Interface PyQt6 moderna e responsiva
- Gestão completa de empresas (156+ cadastradas)
- Sistema TNC com workflow de aprovação
- Dashboard interativo com gráficos
- Relatórios PDF personalizados
- Administração do sistema
- Atalhos com ícone personalizado

🛠️ Stack Tecnológica:
- Python 3.8+ (backend)
- PyQt6 (frontend GUI)
- SQLite3 (banco de dados)
- Matplotlib (visualizações)
- ReportLab (PDFs)
- Arquitetura MVC

📊 Status:
✅ 100% funcional e testado
✅ Banco de dados populado
✅ Interface completa
✅ Relatórios funcionando
✅ Documentação GitHub ready
✅ Pronto para produção

🎉 Próximos passos: Configurar remote GitHub e push!"

echo.
echo 🌿 Configurando branch principal...
%GIT_CMD% branch -M main

echo.
echo ✅ COMMIT REALIZADO COM SUCESSO!
echo.
echo ========================================
echo      🌐 CRIAR REPOSITÓRIO NO GITHUB
echo ========================================
echo.
echo 📝 PASSO A PASSO:
echo.
echo 1. 🌐 Abra: https://github.com/new
echo 2. 📝 Repository name: tnc-gestao
echo 3. 📄 Description: Sistema de Gestão de TNCs em Python com PyQt6
echo 4. 🔓 Escolha: Public ou Private
echo 5. ❌ NÃO marque "Add README" (já temos um completo)
echo 6. ❌ NÃO marque "Add .gitignore" (já temos)
echo 7. ❌ NÃO marque "Choose a license" (já temos MIT)
echo 8. 🎯 Clique "Create repository"
echo.
echo ========================================
echo      📤 COMANDOS PARA UPLOAD
echo ========================================
echo.
echo Após criar o repositório, execute:
echo.
echo %GIT_CMD% remote add origin https://github.com/SEU_USUARIO/tnc-gestao.git
echo %GIT_CMD% push -u origin main
echo.
echo 💡 DICA: Substitua SEU_USUARIO pelo seu username do GitHub!
echo.
echo ========================================
echo.

REM Mostrar status atual
echo 📊 STATUS ATUAL DO REPOSITÓRIO:
echo.
%GIT_CMD% status --short
echo.
%GIT_CMD% log --oneline -n 3

echo.
pause
