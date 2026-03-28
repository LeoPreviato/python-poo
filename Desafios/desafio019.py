from rich import print
from time import sleep

class Livro:
    """
    Representa um livro com título, total de páginas e página atual.
    
    Attributes:
        titulo (str): Título do livro.
        total_paginas (int): Número total de páginas do livro.
        pagina_atual (int): Página atual em que o usuário está lendo.
    """
    
    def __init__(self, titulo, paginas):
        """
        Inicializa um novo livro e imprime uma mensagem de abertura.
        
        Args:
            titulo (str): Título do livro.
            paginas (int): Número total de páginas do livro.
        """
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f"[blue]Você acabou de abrir o livro [red]'{self.titulo}'[/] que tem [green]{self.total_paginas} páginas[/] no total. Você agora está na[/] [yellow]página {self.pagina_atual}[/]")

    def avancar_pagina(self, quantidade=1):
        """
        Avança a página atual por uma quantidade especificada e imprime o progresso.
        
        Args:
            quantidade (int, optional): Número de páginas a avançar. Padrão é 1.
        """
        cont = 1
        for pagina in range(0, quantidade, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual}", end=" ▶︎ ")
                sleep(0.2)
                cont += 1
        print(f"[blue]Você avancou {cont} páginas e agora está na[/] [yellow]página {self.pagina_atual}[/]")

        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao fim do livro '{self.titulo}'[/]")

    def fim_do_livro(self) -> bool:
        """
        Verifica se o usuário chegou ao fim do livro.
        
        Returns:
            bool: True se a página atual for igual ao total de páginas, False caso contrário.
        """
        return True if self.pagina_atual == self.total_paginas else False


livro1 = Livro("O Senhor dos Anéis", 20)
livro1.avancar_pagina(19)
