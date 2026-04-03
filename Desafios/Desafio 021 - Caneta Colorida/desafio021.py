from rich import print

class Caneta:
    """
    Classe que representa uma caneta com cores e estados (tampada/destampada).

    Atributos:
        cor (str): Código de cor formatado para exibição com rich (ex: "[blue]").
        caneta_tampada (bool): Indica se a caneta está tampada (True) ou destampada (False).
    """

    def __init__(self, cor = "azul"):
        """
        Inicializa uma nova caneta com cor especificada.

        Args:
            cor (str): Cor da caneta ("azul", "vermelho", "vermelha", "verde").
                       Padrão é "azul". Cores não reconhecidas resultam em branco.
        """
        escolha_cor = ""
        match cor.lower().strip():
            case "azul":
                escolha_cor = "[blue]"
            case "vermelho" | "vermelha":
                escolha_cor = "[red]"
            case "verde":
                escolha_cor = "[green]"
            case _:
                escolha_cor = "[white]"
        self.cor = escolha_cor
        self.caneta_tampada = True

    def escrever_mensagem(self, texto):
        """
        Escreve uma mensagem colorida se a caneta estiver destampada.

        Args:
            texto (str): Texto a ser escrito.

        Nota: Se a caneta estiver tampada, exibe uma mensagem de aviso.
        """
        if self.caneta_tampada:
            print(f":prohibited: A {self.cor}caneta[/] está tampada. Destampe-a para escrever.")
        else:
            print(f"{self.cor}{texto}[/]", end=" ")

    def pular_linha(self, quantidade = 1):
        """
        Pula linhas na tela.

        Args:
            quantidade (int): Número de linhas a pular. Padrão é 1.
        """
        print("\n" * quantidade, end="")

    def tampar_caneta(self):
        """Tampa a caneta impedindo que escreva."""
        self.caneta_tampada = True

    def destampar_caneta(self):
        """Destampa a caneta permitindo que escreva."""
        self.caneta_tampada = False

caneta1 = Caneta("azul")
caneta2 = Caneta("vermelha")
caneta3 = Caneta("verde")

caneta1.destampar_caneta()
caneta2.destampar_caneta()
caneta3.destampar_caneta()

caneta1.escrever_mensagem("Olá, Mundo!")
caneta2.escrever_mensagem("Testando!")
caneta3.escrever_mensagem("Caneta verde aqui!")