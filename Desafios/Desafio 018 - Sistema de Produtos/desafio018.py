from rich import print
from rich.panel import Panel

class Churrasco:
    """
    Representa um churrasco com nome e quantidade de pessoas.
    
    Attributes:
        nome_churrasco (str): Nome do churrasco.
        quantidade_pessoas (int): Número de pessoas participantes.
    """
    
    def __init__(self, nome_churrasco, quantidade_pessoas):
        """
        Inicializa um novo churrasco.
        
        Args:
            nome_churrasco (str): Nome do churrasco.
            quantidade_pessoas (int): Número de pessoas participantes.
        """
        self.nome_churrasco = nome_churrasco
        self.quantidade_pessoas = quantidade_pessoas

    def analisar_churrasco(self):
        """
        Analisa o churrasco e imprime um painel com informações sobre consumo de carne e custos.
        
        Calcula o total de carne necessário baseado em 0.4kg por pessoa,
        o custo total e o valor dividido por pessoa. Imprime um painel formatado
        com essas informações. Se a quantidade de pessoas for menor ou igual a zero,
        exibe uma mensagem de erro e retorna sem calcular.
        """
        if self.quantidade_pessoas <= 0:
            print("[red]ERRO: A quantidade de pessoas deve ser maior que zero![/]")
            return

        consumo_carne = 0.4
        preco_kg = 82.40

        total_carne = self.quantidade_pessoas * consumo_carne
        valor_total = total_carne * preco_kg
        valor_dividido_pessoas = valor_total / self.quantidade_pessoas

        texto = (
            f"Analisando [green]{self.nome_churrasco}[/] com [blue]{self.quantidade_pessoas} convidados[/]...\n\n"
            f"Cada participante comerá {consumo_carne:.1f}kg de carne, e cada kg custa R${preco_kg:.2f}\n\n"
            f"Recomendamos comprar [blue]{total_carne:.3f}kg[/] de carne\n\n"
            f"O custo total será de [green]R${valor_total:.2f}[/]\n\n"
            f"Cada pessoa pagará aproximadamente [yellow]R${valor_dividido_pessoas:.2f}[/] para participar"
        )

        painel = Panel(texto, title=f":poultry_leg: {self.nome_churrasco}")

        print(painel)

c1 = Churrasco("Churras dos Cria", 15)

c1.analisar_churrasco()