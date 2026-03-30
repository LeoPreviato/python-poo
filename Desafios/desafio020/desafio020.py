from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nickname):
        self.nome = nome
        self.nome_de_jogo = nickname
        self.jogos = []

    def adicionar_jogo(self, *jogo):
        for jogos in jogo:
            self.jogos.append(jogos)

    def ficha(self):
        lista_jogos = "\n:video_game: ".join(self.jogos)
        print(Panel(
            f"Nome real: [black on blue]{self.nome}[/]\nJogos favoritos:\n:video_game: [blue]{lista_jogos}[/]",
            title=f"Ficha do(a) jogador(a) <{self.nome_de_jogo}>", width=45
        ))

jogador1 = Gamer("Leonardo", "Danike")
jogador1.adicionar_jogo("Spider-Man 2")
jogador1.adicionar_jogo("Good of War Ragnarok")
jogador1.adicionar_jogo("Forza Horizon 5")
jogador1.ficha()

jogador2 = Gamer("Bruna", "Bumpy")
jogador2.adicionar_jogo("Among Us")
jogador2.adicionar_jogo("Minecraft")
jogador2.adicionar_jogo("Roblox")
jogador2.ficha()
