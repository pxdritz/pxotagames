import random

class JogoDaVelha:
    def __init__(self, nivel=1):
        self.tabuleiro = [' ' for _ in range(9)]
        self.nivel = nivel  # 1=Fácil, 2=Médio, 3=Difícil
        self.humano = 'X'
        self.cpu = 'O'

    def exibir_tabuleiro(self):
        print("\n")
        for i in range(3):
            print(f" {self.tabuleiro[i*3]} | {self.tabuleiro[i*3+1]} | {self.tabuleiro[i*3+2]} ")
            if i < 2:
                print("-----------")
        print("\n")

    def espacos_livres(self):
        return [i for i, spot in enumerate(self.tabuleiro) if spot == ' ']

    def verificar_vencedor(self, jogador):
        combinacoes = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]              # Diagonais
        ]
        for combo in combinacoes:
            if all(self.tabuleiro[i] == jogador for i in combo):
                return True
        return False

    def movimento_humano(self):
        while True:
            try:
                pos = int(input("Escolha uma posição (0-8): "))
                if pos < 0 or pos > 8:
                    print("Posição inválida! Digite entre 0 e 8.")
                    continue
                if self.tabuleiro[pos] != ' ':
                    print("Essa posição já está ocupada!")
                    continue
                self.tabuleiro[pos] = self.humano
                break
            except ValueError:
                print("Digite um número válido!")

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
        print(f"CPU jogou em: {pos}")

    def _cpu_medio(self):
        # Tenta ganhar
        for pos in self.espacos_livres():
            self.tabuleiro[pos] = self.cpu
            if self.verificar_vencedor(self.cpu):
                print(f"CPU jogou em: {pos}")
                return
            self.tabuleiro[pos] = ' '

        # Tenta bloquear
        for pos in self.espacos_livres():
            self.tabuleiro[pos] = self.humano
            if self.verificar_vencedor(self.humano):
                self.tabuleiro[pos] = self.cpu
                print(f"CPU jogou em: {pos}")
                return
            self.tabuleiro[pos] = ' '

        # Senão, escolhe aleatoriamente
        pos = random.choice(self.espacos_livres())
        self.tabuleiro[pos] = self.cpu
        print(f"CPU jogou em: {pos}")

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
        print(f"CPU jogou em: {melhor_movimento}")

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

    def jogar(self):
        print("=== JOGO DA VELHA ===")
        print("Posições do tabuleiro (0-8):")
        print(" 0 | 1 | 2\n-----------\n 3 | 4 | 5\n-----------\n 6 | 7 | 8\n")

        while True:
            self.exibir_tabuleiro()

            # Movimento do humano
            self.movimento_humano()
            if self.verificar_vencedor(self.humano):
                self.exibir_tabuleiro()
                print("🎉 Você venceu!")
                break
            if not self.espacos_livres():
                self.exibir_tabuleiro()
                print("🤝 Empate!")
                break

            # Movimento da CPU
            self.movimento_cpu()
            if self.verificar_vencedor(self.cpu):
                self.exibir_tabuleiro()
                print("🤖 CPU venceu!")
                break
            if not self.espacos_livres():
                self.exibir_tabuleiro()
                print("🤝 Empate!")
                break

def main():
    while True:
        print("\n=== JOGO DA VELHA ===")
        print("Escolha o nível da CPU:")
        print("1 - Fácil (movimentos aleatórios)")
        print("2 - Médio (tenta ganhar/bloquear)")
        print("3 - Difícil (IA perfeita)")

        try:
            nivel = int(input("Digite 1, 2 ou 3: "))
            if nivel not in [1, 2, 3]:
                print("Opção inválida!")
                continue
        except ValueError:
            print("Digite um número válido!")
            continue

        jogo = JogoDaVelha(nivel)
        jogo.jogar()

        jogar_novamente = input("\nJogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Até logo!")
            break

if __name__ == "__main__":
    main()
