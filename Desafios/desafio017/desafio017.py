from rich import print
from rich.panel import Panel

class Produto:
    """
    Representa um produto com nome e preço.
    
    Attributes:
        nome (str): Nome do produto.
        preco (float): Preço do produto.
    """
    
    def __init__(self, nome, preco):
        """
        Inicializa um novo produto.
        
        Args:
            nome (str): Nome do produto.
            preco (float): Preço do produto.
        """
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        """
        Imprime uma etiqueta formatada do produto usando um painel.
        
        A etiqueta inclui o nome do produto, uma linha separadora e o preço formatado.
        """
        caixa = Panel(f"{self.nome:^30}\n{"":-^30}\n{self.preco:.^30,.2f}",title="Produto",width=35)
        print(caixa)

produto1 = Produto("Macbook Air M4", 6_000.00)
produto2 = Produto("Iphone 13", 4_000.00)

produto1.etiqueta()
produto2.etiqueta()
