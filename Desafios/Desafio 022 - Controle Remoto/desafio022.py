from rich import print
from rich.console import Console
from rich.panel import Panel

class ControleRemoto:
    """
    Classe que simula um controle remoto para uma TV.

    Atributos de classe:
        canal_minimo (int): Menor número de canal disponível (1).
        canal_maximo (int): Maior número de canal disponível (5).
        volume_minimo (int): Menor nível de volume (1).
        volume_maximo (int): Maior nível de volume (6).

    Atributos de instância:
        canal_atual (int): Canal atualmente sintonizado.
        volume_atual (int): Nível de volume atual.
        tv_ligada (bool): Estado da TV (ligada ou desligada).
    """

    canal_minimo: int = 1
    canal_maximo: int = 5
    volume_minimo: int = 1
    volume_maximo: int = 6

    def __init__(self, canal = 1, volume = 2):
        """
        Inicializa um novo controle remoto.

        Args:
            canal (int): Canal inicial. Padrão é 1.
            volume (int): Volume inicial. Padrão é 2.
        """
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.tv_ligada: bool = False

    def ligar_desligar_tv(self):
        """Alterna o estado da TV entre ligada e desligada."""
        self.tv_ligada = not self.tv_ligada

    def aumentar_canal(self):
        """
        Aumenta o canal em uma unidade se a TV estiver ligada.
        Se atingir o canal máximo, volta ao canal mínimo (efeito cíclico).
        """
        if self.tv_ligada:
            if self.canal_atual == ControleRemoto.canal_maximo:
                self.canal_atual = ControleRemoto.canal_minimo
            else:
                self.canal_atual += 1

    def diminuir_canal(self):
        """
        Diminui o canal em uma unidade se a TV estiver ligada.
        Se atingir o canal mínimo, volta ao canal máximo (efeito cíclico).
        """
        if self.tv_ligada:
            if self.canal_atual == ControleRemoto.canal_minimo:
                self.canal_atual = ControleRemoto.canal_maximo
            else:
                self.canal_atual -= 1

    def aumentar_volume(self):
        """Aumenta o volume em uma unidade se a TV estiver ligada e não estiver no máximo."""
        if self.tv_ligada:
            if self.volume_atual != ControleRemoto.volume_maximo:
                self.volume_atual += 1

    def diminuir_volume(self):
        """Diminui o volume em uma unidade se a TV estiver ligada e não estiver no mínimo."""
        if self.tv_ligada:
            if self.volume_atual != ControleRemoto.volume_minimo:
                self.volume_atual -= 1

    def mostrar_tv(self):
        """
        Exibe o estado atual da TV em um painel formatado.

        Se a TV estiver desligada, mostra mensagem de desligada.
        Se estiver ligada, exibe canal atual (em destaque) e barra de volume.
        """
        if not self.tv_ligada:
            conteudo_panel = f":prohibited:[red]A TV está desligada.[/]"
        else:
            conteudo_panel = "CANAL  = "

            for canal in range(ControleRemoto.canal_minimo, ControleRemoto.canal_maximo + 1):
                if canal == self.canal_atual:
                    conteudo_panel += f"[yellow on yellow] {canal} [/]"
                else:
                    conteudo_panel += f" {canal}"
            conteudo_panel += "\nVOLUME = "

            for volume in range(ControleRemoto.volume_minimo, ControleRemoto.volume_maximo + 1):
                if volume <= self.volume_atual:
                    conteudo_panel += "[black on cyan] [/]"
                else:
                    conteudo_panel += "[black on white] [/]"

        tv = Panel(conteudo_panel, title="[ TV ]", width=30)
        print(tv)

console = Console()

controle = ControleRemoto()
while True:
    controle.mostrar_tv()
    comando_controle = str(input(f"< CANAL {controle.canal_atual} > | - VOLUME {controle.volume_atual} + | LIGAR/DESLIGAR (@) | SAIR (0): ")).lower().strip()

    match comando_controle:
        case "<":
            controle.diminuir_canal()
        case ">":
            controle.aumentar_canal()
        case "-":
            controle.diminuir_volume()
        case "+":
            controle.aumentar_volume()
        case "@":
            controle.ligar_desligar_tv()
        case "0":
            break
    console.clear()
