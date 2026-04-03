from rich import print
from rich.panel import Panel

class Gamer:
    """
    Classe que representa um jogador de vídeo games.

    Atributos:
        nome (str): Nome real do jogador.
        nome_de_jogo (str): Nickname ou apelido do jogador.
        jogos (list): Lista de jogos favoritos do jogador.
    """

    def __init__(self, nome, nickname):
        """
        Inicializa um novo objeto Gamer.

        Args:
            nome (str): Nome real do jogador.
            nickname (str): Nome de jogo (apelido) do jogador.
        """
        self.nome = nome
        self.nome_de_jogo = nickname
        self.jogos = list()

    def adicionar_jogo(self, games):
        """
        Adiciona um jogo à lista de favoritos do jogador e ordena alfabeticamente.

        Args:
            games (str): Nome do jogo a ser adicionado.
        """
        self.jogos.append(games)
        self.jogos = sorted(self.jogos, key=str.lower)

    def ficha(self):
        """
        Exibe a ficha do jogador com seus dados e lista de jogos favoritos em um painel formatado.
        """
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
