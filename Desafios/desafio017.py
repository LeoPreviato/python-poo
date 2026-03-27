from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        caixa = Panel(f"{self.nome:^30}\n{"":-^30}\n{self.preco:.^30,.2f}",title="Produto",width=35)
        print(caixa)

produto1 = Produto("Macbook Air M4", 6_000.00)
produto2 = Produto("Iphone 13", 4_000.00)

produto1.etiqueta()
produto2.etiqueta()
