import pygame
import sys
import random

# --- Lógica do Jogo da Velha ---
class JogoDaVelha:
    def __init__(self, nivel=1):
        self.tabuleiro = [' ' for _ in range(9)]
        self.nivel = nivel  # 1=Fácil, 2=Médio, 3=Difícil
        self.humano = 'X'
        self.cpu = 'O'

    def espacos_livres(self):
        return [i for i, spot in enumerate(self.tabuleiro) if spot == ' ']

    def verificar_vencedor(self, jogador):
        combinacoes = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in combinacoes:
            if all(self.tabuleiro[i] == jogador for i in combo):
                return True
        return False

    def movimento_cpu(self):
        if self.nivel == 1:
            self._cpu_facil()
        elif self.nivel == 2:
            self._cpu_medio()
        else:
            self._cpu_dificil()

    def _cpu_facil(self):
        pos = random.choice(self.espacos_livres())
        self.tabuleiro[pos] = self.cpu

    def _cpu_medio(self):
        for pos in self.espacos_livres():
            self.tabuleiro[pos] = self.cpu
            if self.verificar_vencedor(self.cpu):
                return
            self.tabuleiro[pos] = ' '
        for pos in self.espacos_livres():
            self.tabuleiro[pos] = self.humano
            if self.verificar_vencedor(self.humano):
                self.tabuleiro[pos] = self.cpu
                return
            self.tabuleiro[pos] = ' '
        self._cpu_facil()

    def _cpu_dificil(self):
        melhor_score = float('-inf')
        melhor_movimento = None
        for pos in self.espacos_livres():
            self.tabuleiro[pos] = self.cpu
            score = self.minimax(0, False)
            self.tabuleiro[pos] = ' '
            if score > melhor_score:
                melhor_score = score
                melhor_movimento = pos
        self.tabuleiro[melhor_movimento] = self.cpu

    def minimax(self, profundidade, eh_cpu):
        if self.verificar_vencedor(self.cpu):
            return 10 - profundidade
        if self.verificar_vencedor(self.humano):
            return profundidade - 10
        if not self.espacos_livres():
            return 0
        if eh_cpu:
            melhor_score = float('-inf')
            for pos in self.espacos_livres():
                self.tabuleiro[pos] = self.cpu
                score = self.minimax(profundidade + 1, False)
                self.tabuleiro[pos] = ' '
                melhor_score = max(score, melhor_score)
            return melhor_score
        else:
            pior_score = float('inf')
            for pos in self.espacos_livres():
                self.tabuleiro[pos] = self.humano
                score = self.minimax(profundidade + 1, True)
                self.tabuleiro[pos] = ' '
                pior_score = min(score, pior_score)
            return pior_score

# --- Interface Gráfica com pygame ---
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 120, 215)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)
CINZA = (200, 200, 200)
LARGURA, ALTURA = 400, 540
TAMANHO_CELULA = 120
MARGEM = 20

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo da Velha')
fonte = pygame.font.SysFont(None, 60)
fonte_pequena = pygame.font.SysFont(None, 36)


def desenhar_tabuleiro(jogo, selecionado=None):
    tela.fill(BRANCO)
    for i in range(1, 3):
        pygame.draw.line(tela, PRETO, (MARGEM, MARGEM + i*TAMANHO_CELULA), (LARGURA-MARGEM, MARGEM + i*TAMANHO_CELULA), 4)
        pygame.draw.line(tela, PRETO, (MARGEM + i*TAMANHO_CELULA, MARGEM), (MARGEM + i*TAMANHO_CELULA, MARGEM+3*TAMANHO_CELULA), 4)
    for i in range(3):
        for j in range(3):
            idx = i*3 + j
            x = MARGEM + j*TAMANHO_CELULA
            y = MARGEM + i*TAMANHO_CELULA
            cor = CINZA if selecionado == idx else BRANCO
            pygame.draw.rect(tela, cor, (x+4, y+4, TAMANHO_CELULA-8, TAMANHO_CELULA-8))
            if jogo.tabuleiro[idx] == 'X':
                texto = fonte.render('X', True, AZUL)
                tela.blit(texto, (x + TAMANHO_CELULA//2 - texto.get_width()//2, y + TAMANHO_CELULA//2 - texto.get_height()//2))
            elif jogo.tabuleiro[idx] == 'O':
                texto = fonte.render('O', True, VERMELHO)
                tela.blit(texto, (x + TAMANHO_CELULA//2 - texto.get_width()//2, y + TAMANHO_CELULA//2 - texto.get_height()//2))

def desenhar_status(mensagem):
    barra = pygame.Rect(0, 400, LARGURA, 100)
    pygame.draw.rect(tela, BRANCO, barra)
    texto = fonte_pequena.render(mensagem, True, PRETO)
    tela.blit(texto, (LARGURA//2 - texto.get_width()//2, 430))

def desenhar_botoes_nivel(nivel_atual):
    botoes = []
    textos = ['Fácil', 'Médio', 'Difícil']
    for i, txt in enumerate(textos):
        cor = VERDE if nivel_atual == i+1 else CINZA
        btn = pygame.Rect(30 + i*120, 480, 100, 40)
        pygame.draw.rect(tela, cor, btn)
        pygame.draw.rect(tela, PRETO, btn, 2)
        texto = fonte_pequena.render(txt, True, PRETO)
        tela.blit(texto, (btn.x + btn.width//2 - texto.get_width()//2, btn.y + btn.height//2 - texto.get_height()//2))
        botoes.append(btn)
    return botoes

def main():
    nivel = 2
    jogo = JogoDaVelha(nivel=nivel)
    rodando = True
    fim = False
    mensagem = 'Sua vez!'
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # Clique nos botões de nível
                botoes = desenhar_botoes_nivel(nivel)
                for i, btn in enumerate(botoes):
                    if btn.collidepoint(mx, my):
                        nivel = i+1
                        jogo = JogoDaVelha(nivel=nivel)
                        fim = False
                        mensagem = 'Sua vez!'
                if not fim and MARGEM < mx < LARGURA-MARGEM and MARGEM < my < MARGEM+3*TAMANHO_CELULA:
                    col = (mx - MARGEM) // TAMANHO_CELULA
                    lin = (my - MARGEM) // TAMANHO_CELULA
                    idx = lin*3 + col
                    if jogo.tabuleiro[idx] == ' ':
                        jogo.tabuleiro[idx] = 'X'
                        if jogo.verificar_vencedor('X'):
                            mensagem = 'Você venceu!'
                            fim = True
                        elif not jogo.espacos_livres():
                            mensagem = 'Empate!'
                            fim = True
                        else:
                            jogo.movimento_cpu()
                            if jogo.verificar_vencedor('O'):
                                mensagem = 'CPU venceu!'
                                fim = True
                            elif not jogo.espacos_livres():
                                mensagem = 'Empate!'
                                fim = True
        desenhar_tabuleiro(jogo)
        desenhar_status(mensagem)
        desenhar_botoes_nivel(nivel)
        pygame.display.flip()
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
