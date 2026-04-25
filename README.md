# 🎮 Meus Jogos em Python

Uma coleção de jogos e aplicações criados com Python e Pygame.

## 🎯 Projetos

### 1. **Jogo da Velha contra CPU** (`teste.py`)
Jogo da velha clássico contra uma CPU com 3 níveis de dificuldade:
- 🟢 **Fácil**: CPU faz movimentos aleatórios
- 🟡 **Médio**: CPU tenta ganhar e bloqueia seus movimentos
- 🔴 **Difícil**: IA perfeita com algoritmo Minimax (nunca perde)

**Como jogar:**
```bash
python3 teste.py
```
- Clique nos botões para escolher o nível
- Clique nas casas do tabuleiro para jogar
- Pressione "Jogar Novamente" para reiniciar

---

### 2. **Jogo da Cobrinha** (`snake_game.py`)
Clássico jogo Snake com a imagem personalizada como cabeça da cobra.

**Recursos:**
- 🐍 Cabeça da cobra com imagem possível de personalizar
- 🍎 Comida aleatória
- 📈 Pontuação que aumenta
- ⚡ Velocidade progressiva
- 🎮 Controles simples com setas do teclado

**Como jogar:**
```bash
python3 snake_game.py
```

**Controles:**
- ⬆️ ⬇️ ⬅️ ➡️ Setas do teclado para mover
- **R** para reiniciar após game over
- **Q** para sair

---

## 📋 Requisitos

- Python 3.7+
- pygame
- numpy

## 🚀 Instalação

### Windows

1. **Instalar Python** (se não tiver): [python.org](https://www.python.org/downloads/)

2. **Clonar o repositório:**
```bash
git clone https://github.com/pxdritz/pxotagames
cd pxotagames
```

3. **Criar ambiente virtual (recomendado):**
```bash
python -m venv venv
venv\Scripts\activate
```

4. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

5. **Rodar um jogo:**
```bash
python velha.py
python cobrinha.py
```

---

### Linux / macOS

1. **Instalar Python** (se não tiver):
```bash
# Linux (Ubuntu/Debian)
sudo apt-get install python3 python3-pip python3-venv

# macOS
brew install python3
```

2. **Clonar o repositório:**
```bash
git clone https://github.com/pxdritz/pxotagames
cd pxotagames
```

3. **Criar ambiente virtual:**
```bash
python3 -m venv venv
source venv/bin/activate
```

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
├── imagempersonalizadaqtuquerbobao.png              # Imagem da cobra
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

## 🔧 Solução de Problemas

### "ModuleNotFoundError: No module named 'pygame'"
```bash
pip install pygame
```

### "ModuleNotFoundError: No module named 'numpy'"
```bash
pip install numpy
```

### PyAudio não funciona no macOS
```bash
brew install portaudio
pip install pyaudio
```

### Snake_game.py não encontra a imagem
- Certifique-se que `pxota.png` está no mesmo diretório que `snake_game.py`
- Ou atualize o caminho em `snake_game.py` linha 68

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
