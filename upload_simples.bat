@echo off
echo ========================================
echo    UPLOAD TNC GESTAO PARA GITHUB
echo ========================================

cd /d "d:\tnc-gestao"

echo Configurando repositorio...
git remote remove origin 2>nul
git remote add origin https://github.com/Everton-G-Costa/TNC_GESTAO.git

echo.
echo Fazendo push...
git push -u origin main

echo.
if %errorlevel% equ 0 (
    echo ✓ SUCESSO! Projeto enviado para:
    echo   https://github.com/Everton-G-Costa/TNC_GESTAO
) else (
    echo ❌ Erro no push. Pode ser necessario:
    echo 1. Fazer login no GitHub
    echo 2. Configurar autenticacao
    echo 3. Verificar permissoes
)

pause
