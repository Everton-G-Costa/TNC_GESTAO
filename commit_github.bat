@echo off
echo.
echo ========================================
echo   📦 COMMIT TNC GESTÃO PARA GITHUB
echo ========================================
echo.

REM Tentar diferentes formas de detectar Git
set GIT_FOUND=0

REM Método 1: git no PATH
git --version >nul 2>&1
if %errorlevel% equ 0 (
    set GIT_FOUND=1
    echo ✅ Git encontrado no PATH!
    goto :git_commands
)

REM Método 2: Git comum no Program Files
if exist "C:\Program Files\Git\bin\git.exe" (
    set GIT_PATH="C:\Program Files\Git\bin\git.exe"
    set GIT_FOUND=1
    echo ✅ Git encontrado em: %GIT_PATH%
    goto :git_commands
)

REM Método 3: Git x86 no Program Files
if exist "C:\Program Files (x86)\Git\bin\git.exe" (
    set GIT_PATH="C:\Program Files (x86)\Git\bin\git.exe"
    set GIT_FOUND=1
    echo ✅ Git encontrado em: %GIT_PATH%
    goto :git_commands
)

REM Git não encontrado
echo ❌ Git não está instalado!
echo.
echo 🔧 OPÇÕES PARA CONTINUAR:
echo.
echo 📋 OPÇÃO 1 - GITHUB DESKTOP (MAIS FÁCIL):
echo    1. Baixe: https://desktop.github.com/
echo    2. Instale e faça login no GitHub
echo    3. Clique: "Add an Existing Repository from your Hard Drive"
echo    4. Selecione: D:\tnc-gestao
echo    5. Commit: "Sistema TNC Gestão completo"
echo    6. Publish repository: "tnc-gestao"
echo.
echo 📋 OPÇÃO 2 - INSTALAR GIT:
echo    1. Baixe: https://git-scm.com/download/windows
echo    2. Instale com configurações padrão
echo    3. Execute este script novamente
echo.
echo 📋 OPÇÃO 3 - UPLOAD MANUAL:
echo    1. Vá para: https://github.com/new
echo    2. Crie repositório: "tnc-gestao"
echo    3. Arraste arquivos da pasta para o GitHub
echo.
pause
exit /b 1

:git_commands
echo.
echo 🔧 Configurando repositório Git...
echo.

REM Usar git do PATH ou caminho específico
if defined GIT_PATH (
    set GIT_CMD=%GIT_PATH%
) else (
    set GIT_CMD=git
)

REM Verificar se já é um repositório
if exist ".git" (
    echo 📁 Repositório Git já existe.
    goto :commit_changes
)

REM Inicializar repositório
echo 📦 Inicializando repositório Git...
%GIT_CMD% init
if %errorlevel% neq 0 (
    echo ❌ Erro ao inicializar repositório!
    pause
    exit /b 1
)

REM Configurar usuário se necessário
%GIT_CMD% config user.name >nul 2>&1
if %errorlevel% neq 0 (
    set /p git_name=📝 Digite seu nome para Git: 
    %GIT_CMD% config user.name "!git_name!"
)

%GIT_CMD% config user.email >nul 2>&1
if %errorlevel% neq 0 (
    set /p git_email=📧 Digite seu email para Git: 
    %GIT_CMD% config user.email "!git_email!"
)

:commit_changes
echo.
echo 📦 Adicionando arquivos...
%GIT_CMD% add .
if %errorlevel% neq 0 (
    echo ❌ Erro ao adicionar arquivos!
    pause
    exit /b 1
)

echo.
echo 💾 Fazendo commit...
%GIT_CMD% commit -m "Sistema TNC Gestão - Versão Python funcional completa

✨ Funcionalidades implementadas:
- Interface PyQt6 completa e responsiva
- Gestão de empresas (156+ já cadastradas)
- Sistema TNC com workflow completo de aprovação
- Dashboard interativo com gráficos (Matplotlib)
- Relatórios PDF personalizados (ReportLab)
- Administração completa do sistema
- Atalhos com ícone personalizado

🛠️ Tecnologias utilizadas:
- Python 3.8+ (linguagem principal)
- PyQt6 (interface gráfica moderna)
- SQLite3 (banco de dados local)
- Matplotlib (gráficos e visualizações)
- ReportLab (geração de PDFs)
- Arquitetura MVC limpa e escalável

📊 Status do projeto:
- ✅ Sistema 100% funcional e testado
- ✅ Interface gráfica completa
- ✅ Banco de dados populado e estável
- ✅ Relatórios funcionando perfeitamente
- ✅ Documentação completa para GitHub
- ✅ Pronto para produção

🎯 Próximos passos:
- Configurar repositório remoto no GitHub
- Publicar para a comunidade
- Aceitar contribuições

Desenvolvido com ❤️ em Python"

if %errorlevel% neq 0 (
    echo ❌ Erro ao fazer commit!
    pause
    exit /b 1
)

echo.
echo 🔧 Configurando branch principal...
%GIT_CMD% branch -M main
if %errorlevel% neq 0 (
    echo ⚠️ Aviso: Não foi possível renomear branch (isso é normal)
)

echo.
echo ✅ Commit realizado com sucesso!
echo.
echo ========================================
echo      🌐 PRÓXIMOS PASSOS NO GITHUB
echo ========================================
echo.
echo 1. 🌐 Vá para: https://github.com
echo 2. 🔑 Faça login na sua conta
echo 3. ➕ Clique em "New repository"
echo 4. 📝 Preencha:
echo    - Repository name: tnc-gestao
echo    - Description: Sistema de Gestão de TNCs em Python com PyQt6
echo    - Public ou Private (sua escolha)
echo    - NÃO marque "Add README" (já temos)
echo 5. 🎯 Clique "Create repository"
echo.
echo 💻 Então execute estes comandos:
echo.
echo %GIT_CMD% remote add origin https://github.com/SEU_USUARIO/tnc-gestao.git
echo %GIT_CMD% push -u origin main
echo.
echo ⚠️  IMPORTANTE: Substitua SEU_USUARIO pelo seu nome de usuário do GitHub!
echo.
echo 📋 Para verificar o status:
echo %GIT_CMD% status
echo %GIT_CMD% log --oneline
echo.
echo ========================================
echo.
pause
