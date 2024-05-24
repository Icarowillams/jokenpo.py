class Jokenpo:
    def __init__(self):
        self.jogador1 = ""
        self.jogador2 = ""

    def obterEscolhas(self):
        self.jogador1 = input("Jogador 1, escolha entre pedra, papel ou tesoura: ")
        self.jogador2 = input("Jogador 2, escolha entre pedra, papel ou tesoura: ")

    def determinarVencedor(self):
        if self.jogador1 == self.jogador2:
            print("Empate!")
        elif self.jogador1 == "pedra":
            if self.jogador2 == "tesoura":
                print("Jogador 1 ganha!")
            else:
                print("Jogador 2 ganha!")
        elif self.jogador1 == "papel":
            if self.jogador2 == "pedra":
                print("Jogador 1 ganha!")
            else:
                print("Jogador 2 ganha!")
        elif self.jogador1 == "tesoura":
            if self.jogador2 == "papel":
                print("Jogador 1 ganha!")
            else:
                print("Jogador 2 ganha!")
        else:
            print("Escolha inválida. Certifique de digitar 'pedra', 'papel' ou 'tesoura'.")

    def jogar(self):
        while True:
            self.obterEscolhas()
            self.determinarVencedor()
            jogar_novamente = input("Desejam jogar novamente? (s/n): ")
            if jogar_novamente != "s":
                break
jogo = Jokenpo()
jogo.jogar()