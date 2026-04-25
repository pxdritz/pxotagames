import pygame
import random
import os
from enum import Enum

# Inicializar Pygame
pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
COLS = WIDTH // GRID_SIZE
ROWS = HEIGHT // GRID_SIZE
FPS = 5

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (50, 200, 50)
DARK_GREEN = (30, 150, 30)
RED = (200, 50, 50)
YELLOW = (255, 255, 100)
GRAY = (100, 100, 100)

class Direcao(Enum):
    CIMA = (0, -1)
    BAIXO = (0, 1)
    ESQUERDA = (-1, 0)
    DIREITA = (1, 0)

class JogoDaCobrinha:
    def __init__(self, usar_imagem=False):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Jogo da Cobrinha")
        self.clock = pygame.time.Clock()
        self.font_grande = pygame.font.SysFont("Arial", 40, bold=True)
        self.font_media = pygame.font.SysFont("Arial", 25)
        self.font_pequena = pygame.font.SysFont("Arial", 18)
        
        # Estado do jogo
        self.cobra = [(COLS // 2, ROWS // 2)]
        self.direcao = Direcao.DIREITA
        self.proxima_direcao = Direcao.DIREITA
        self.comida = self.gerar_comida()
        self.pontuacao = 0
        self.game_over = False
        self.usar_imagem = usar_imagem
        self.imagem_cabeca = None
        
        # Tentar carregar imagem da cabeça
        if usar_imagem:
            self.carregar_imagem_cabeca()
        
        self.velocidade = FPS

    def carregar_imagem_cabeca(self):
        """Carrega a imagem da cabeça da cobra se existir."""
        try:
            # Procurar por arquivos de imagem no diretório
            for arquivo in os.listdir('.'):
                if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    try:
                        img = pygame.image.load(arquivo)
                        # Redimensionar para tamanho da grade
                        self.imagem_cabeca = pygame.transform.scale(img, (GRID_SIZE, GRID_SIZE))
                        print(f"Imagem carregada: {arquivo}")
                        return
                    except:
                        continue
        except:
            pass
        
        print("Nenhuma imagem encontrada. Usando cabeça verde padrão.")
        self.imagem_cabeca = None

    def gerar_comida(self):
        """Gera uma posição aleatória para a comida."""
        while True:
            pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
            if pos not in self.cobra:
                return pos

    def atualizar(self):
        """Atualiza o estado do jogo."""
        if self.game_over:
            return

        # Atualizar direção
        self.direcao = self.proxima_direcao

        # Calcular nova cabeça
        cabeca_x, cabeca_y = self.cobra[0]
        dx, dy = self.direcao.value
        nova_cabeca = (cabeca_x + dx, cabeca_y + dy)

        # Verificar colisão com paredes
        if (nova_cabeca[0] < 0 or nova_cabeca[0] >= COLS or
            nova_cabeca[1] < 0 or nova_cabeca[1] >= ROWS):
            self.game_over = True
            return

        # Verificar colisão com ela mesma
        if nova_cabeca in self.cobra:
            self.game_over = True
            return

        # Adicionar nova cabeça
        self.cobra.insert(0, nova_cabeca)

        # Verificar se comeu
        if nova_cabeca == self.comida:
            self.pontuacao += 10
            self.comida = self.gerar_comida()
            # Aumentar velocidade a cada 3 comidas
            if self.pontuacao % 30 == 0 and self.velocidade < 20:
                self.velocidade += 1
        else:
            # Remover cauda se não comeu
            self.cobra.pop()

    def desenhar(self):
        """Desenha o jogo."""
        self.screen.fill(BLACK)

        # Desenhar grid de fundo
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, HEIGHT), 1)
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (WIDTH, y), 1)

        # Desenhar corpo da cobra
        for i, (x, y) in enumerate(self.cobra[1:], 1):
            cor = GREEN if i % 2 == 0 else DARK_GREEN
            pygame.draw.rect(self.screen, cor, (x * GRID_SIZE + 2, y * GRID_SIZE + 2, 
                                               GRID_SIZE - 4, GRID_SIZE - 4))

        # Desenhar cabeça
        if self.cobra:
            cabeca_x, cabeca_y = self.cobra[0]
            if self.imagem_cabeca:
                # Desenhar imagem da cabeça
                self.screen.blit(self.imagem_cabeca, (cabeca_x * GRID_SIZE, cabeca_y * GRID_SIZE))
            else:
                # Desenhar cabeça verde padrão
                pygame.draw.rect(self.screen, YELLOW, (cabeca_x * GRID_SIZE + 2, cabeca_y * GRID_SIZE + 2, 
                                                       GRID_SIZE - 4, GRID_SIZE - 4))
                # Olhos
                pygame.draw.circle(self.screen, BLACK, (cabeca_x * GRID_SIZE + 6, cabeca_y * GRID_SIZE + 6), 2)
                pygame.draw.circle(self.screen, BLACK, (cabeca_x * GRID_SIZE + 14, cabeca_y * GRID_SIZE + 6), 2)

        # Desenhar comida
        comida_x, comida_y = self.comida
        pygame.draw.circle(self.screen, RED, (comida_x * GRID_SIZE + GRID_SIZE // 2, 
                                             comida_y * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 2 - 2)

        # Desenhar pontuação
        pontos_texto = self.font_media.render(f"Pontos: {self.pontuacao}", True, WHITE)
        self.screen.blit(pontos_texto, (10, 10))

        # Velocidade
        vel_texto = self.font_pequena.render(f"Velocidade: {self.velocidade}", True, WHITE)
        self.screen.blit(vel_texto, (10, 40))

        # Comprimento
        comp_texto = self.font_pequena.render(f"Comprimento: {len(self.cobra)}", True, WHITE)
        self.screen.blit(comp_texto, (10, 65))

        if self.game_over:
            self.desenhar_game_over()

        pygame.display.flip()

    def desenhar_game_over(self):
        """Desenha a tela de game over."""
        # Fundo semi-transparente
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))

        # Texto
        game_over_texto = self.font_grande.render("GAME OVER", True, RED)
        self.screen.blit(game_over_texto, (WIDTH // 2 - game_over_texto.get_width() // 2, HEIGHT // 2 - 60))

        pontos_texto = self.font_media.render(f"Pontos Finais: {self.pontuacao}", True, WHITE)
        self.screen.blit(pontos_texto, (WIDTH // 2 - pontos_texto.get_width() // 2, HEIGHT // 2))

        comprimento_texto = self.font_media.render(f"Comprimento: {len(self.cobra)}", True, WHITE)
        self.screen.blit(comprimento_texto, (WIDTH // 2 - comprimento_texto.get_width() // 2, HEIGHT // 2 + 50))

        instrucao = self.font_pequena.render("Pressione R para reiniciar ou Q para sair", True, YELLOW)
        self.screen.blit(instrucao, (WIDTH // 2 - instrucao.get_width() // 2, HEIGHT // 2 + 120))

    def reiniciar(self):
        """Reinicia o jogo."""
        self.cobra = [(COLS // 2, ROWS // 2)]
        self.direcao = Direcao.DIREITA
        self.proxima_direcao = Direcao.DIREITA
        self.comida = self.gerar_comida()
        self.pontuacao = 0
        self.game_over = False
        self.velocidade = FPS

    def rodar(self):
        """Loop principal do jogo."""
        rodando = True

        while rodando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direcao != Direcao.BAIXO:
                        self.proxima_direcao = Direcao.CIMA
                    elif event.key == pygame.K_DOWN and self.direcao != Direcao.CIMA:
                        self.proxima_direcao = Direcao.BAIXO
                    elif event.key == pygame.K_LEFT and self.direcao != Direcao.DIREITA:
                        self.proxima_direcao = Direcao.ESQUERDA
                    elif event.key == pygame.K_RIGHT and self.direcao != Direcao.ESQUERDA:
                        self.proxima_direcao = Direcao.DIREITA
                    elif event.key == pygame.K_r and self.game_over:
                        self.reiniciar()
                    elif event.key == pygame.K_q:
                        rodando = False

            self.atualizar()
            self.desenhar()
            self.clock.tick(self.velocidade)

        pygame.quit()

if __name__ == "__main__":
    # Criar jogo tentando carregar imagem
    jogo = JogoDaCobrinha(usar_imagem=True)
    jogo.rodar()
