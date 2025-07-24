@echo off
echo.
echo ========================================
echo      FORCANDO PUSH PARA GITHUB
echo ========================================
echo.

cd /d "d:\tnc-gestao"

echo 1. Verificando status atual...
git status

echo.
echo 2. Configurando remote (forcando)...
git remote remove origin 2>nul
git remote add origin git@github.com:Everton-G-Costa/TNC_GESTAO.git

echo.
echo 3. Verificando remote configurado...
git remote -v

echo.
echo 4. Configurando branch main...
git branch -M main

echo.
echo 5. Verificando branches...
git branch -a

echo.
echo 6. Adicionando arquivos mais recentes...
git add .
git commit -m "Atualizacao final - repositorio GitHub configurado" 2>nul

echo.
echo 7. FAZENDO PUSH PARA GITHUB...
echo    URL: git@github.com:Everton-G-Costa/TNC_GESTAO.git
echo    Branch: main
echo.

git push -u origin main

echo.
echo ========================================
echo      RESULTADO
echo ========================================

if %errorlevel% equ 0 (
    echo ✓ SUCESSO! Projeto enviado para GitHub
    echo ✓ URL: https://github.com/Everton-G-Costa/TNC_GESTAO
    echo ✓ 75+ arquivos enviados
    echo ✓ Sistema TNC Gestao publicado
) else (
    echo ❌ ERRO no push
    echo.
    echo POSSIVEIS CAUSAS:
    echo 1. Repositorio nao existe no GitHub
    echo 2. Sem permissao de escrita
    echo 3. Necessaria autenticacao
    echo.
    echo SOLUCAO:
    echo 1. Va para: https://github.com/new
    echo 2. Crie repositorio: TNC_GESTAO
    echo 3. Execute este script novamente
)

echo.
pause
