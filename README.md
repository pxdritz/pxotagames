# 🎮 Meus Jogos em Python

Uma coleção de jogos criados por mim, Px ;3.

## 🎯 Projetos


### 1. **Jogo da Velha** (`velha.py`)
Jogo da velha clássico contra a CPU com 3 níveis de dificuldade:
- 🟢 **Fácil**: CPU faz movimentos aleatórios
- 🟡 **Médio**: CPU tenta ganhar e bloquear
- 🔴 **Difícil**: CPU perfeita com algoritmo Minimax

**Como jogar:**
```bash
python3 velha.py
```
- Clique nos botões para escolher o nível
- Clique nas casas do tabuleiro para jogar


---

### 2. **Jogo da Cobrinha** (`cobrinha.py`)
Clássico jogo Snake com a imagem personalizada como cabeça da cobra.

**Recursos:**
- 🐍 Cabeça da cobra com imagem possível de personalizar
- 🍎 Comida aleatória
- 📈 Pontuação que aumenta
- ⚡ Velocidade progressiva
- 🎮 Controles simples com setas do teclado

**Como jogar:**
```bash
python3 cobrinha.py
```

**Controles:**
- ⬆️ ⬇️ ⬅️ ➡️ Setas do teclado para mover
- **R** para reiniciar após game over
- **Q** para sair

---

## 📋 Requisitos

- Python 3.7+
- pygame

## 🚀 Instalação

### Windows

1. **Instalar Python** (se não tiver): [python.org](https://www.python.org/downloads/)

2. **Baixe TODOS os arquivos:**
```Clique em "Code" e depois Download Zip
```

3. **Extraia o Zip**
```Aperte com o botão direito no Arquivo e depois em "Extrair"
```

3.5 **Jogue tudo em sua Área de Trabalho ou em qualquer pasta**
```bash
Ctrl+X e Ctrl+V
```

4. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

5. **Rodar um jogo:**
```bash
cd caminho/da/pasta
python velha.py
python cobrinha.py
```

---

### Debian e Ubuntu Based's / macOS

1. **Instalar Python** (se não tiver):
```bash
# Linux
sudo apt-get install python3 python3-pip python3-venv
# na maioria dos Linux's, a única coisa que muda é o gerenciador de pacotes (substitua apt pelo respectivo a sua distro), no Fedora, por exemplo, o gerenciador é o "Dnf"

# macOS
brew install python3
```

2. **Baixe TODOS os arquivos:**
```Clique em "Code" e depois Download Zip
```

3. **Extraia o Zip**
```Aperte com o botão direito no Arquivo e depois em "Extrair"
```

3.5 **Jogue tudo em sua Área de Trabalho ou em qualquer pasta**
```bash
Ctrl+X e Ctrl+V

4. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

5. **Rodar um jogo:**
```bash
python3 velha.py
python3 cobrinha.py
```

---

## 📁 Estrutura do Projeto

```
├── velha.py                 # Jogo da Velha com IA
├── cobrinha.py           # Jogo da Cobrinha
├── pxota.png              # Imagem da cobra
├── requirements.txt        # Dependências do projeto
└── README.md              # Este arquivo
```

---

## 🎮 Como Jogar

### Jogo da Velha
- Escolha um nível de dificuldade
- Clique nas casas vazias para jogar
- X = você, O = CPU
- Ganhe alinhando 3 em linha!

### Jogo da Cobrinha
- Use as setas para mover
- Coma as bolinhas vermelhas
- Evite as paredes e sua própria cauda
- Sua cobra cresce a cada comida

---

## 💡 Melhorias Futuras

- [ ] Adicionar sons aos jogos
- [ ] Leaderboard de pontuação
- [ ] Mais níveis no jogo da cobrinha
- [ ] Tema escuro/claro para interface
- [ ] Suporte para controles do joystick

---

## 📝 Licença

Este projeto está livre para uso pessoal e educacional.

---

## 👤 Autor

Criado por: **pxota**  
Data: 24 de abril de 2026

---

**Divirta-se jogando!** 🎮✨
