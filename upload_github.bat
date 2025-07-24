@echo off
echo.
echo ========================================
echo      UPLOAD PARA GITHUB
echo ========================================
echo.

set GIT_CMD="C:\Program Files\Git\bin\git.exe"

echo Configurando repositorio remoto...
%GIT_CMD% remote remove origin 2>nul
%GIT_CMD% remote add origin https://github.com/Everton-G-Costa/TNC_GESTAO.git

echo.
echo Configurando branch principal...
%GIT_CMD% branch -M main

echo.
echo Verificando remotes configurados...
%GIT_CMD% remote -v

echo.
echo Fazendo push para GitHub...
%GIT_CMD% push -u origin main

echo.
echo ========================================
echo      STATUS FINAL
echo ========================================
echo.

%GIT_CMD% status
echo.

echo ========================================
echo      REPOSITORIO CRIADO!
echo ========================================
echo.
echo URL: https://github.com/Everton-G-Costa/TNC_GESTAO
echo.
echo ✓ 75 arquivos enviados
echo ✓ Sistema TNC Gestao completo
echo ✓ Documentacao GitHub incluida
echo ✓ Pronto para uso e contribuicoes
echo.
pause
