@echo off
echo ===================================
echo Instalador - Meus Jogos em Python
echo ===================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python não está instalado ou não está no PATH!
    echo Por favor, instale Python em https://www.python.org/downloads/
    echo Certifique-se de marcar "Add Python to PATH" durante a instalação
    pause
    exit /b 1
)

echo [OK] Python encontrado!
echo.

REM Criar ambiente virtual
echo Criando ambiente virtual...
python -m venv venv

REM Ativar ambiente virtual
call venv\Scripts\activate.bat

REM Instalar dependências
echo.
echo Instalando dependências...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ===================================
echo Instalação concluída com sucesso!
echo ===================================
echo.
echo Para ativar o ambiente virtual e rodar os jogos, execute:
echo.
echo   venv\Scripts\activate.bat
echo   python velha.py
echo   python cobrinha.py
echo.
pause
