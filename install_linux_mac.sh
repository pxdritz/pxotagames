#!/bin/bash

echo "==================================="
echo "Instalador - Meus Jogos em Python"
echo "==================================="
echo ""

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "[ERRO] Python 3 não está instalado!"
    echo ""
    echo "Para instalar:"
    echo "  Linux (Ubuntu/Debian): sudo apt-get install python3 python3-pip python3-venv"
    echo "  macOS: brew install python3"
    exit 1
fi

echo "[OK] Python $(python3 --version) encontrado!"
echo ""

# Criar ambiente virtual
echo "Criando ambiente virtual..."
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
echo ""
echo "Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "==================================="
echo "Instalação concluída com sucesso!"
echo "==================================="
echo ""
echo "Para ativar o ambiente virtual e rodar os jogos, execute:"
echo ""
echo "  source venv/bin/activate"
echo "  python3 velha.py"
echo "  python3 cobrinha.py"
echo ""
