from rich import print

class Funcionario:
    """
    Representa um funcionário da empresa.
    
    Attributes:
        nome (str): Nome do funcionário.
        setor (str): Setor onde o funcionário trabalha.
        cargo (str): Cargo/posição do funcionário na empresa.
    """
    
    def __init__(self, nome, setor, cargo):
        """
        Inicializa um novo funcionário.
        
        Args:
            nome (str): Nome do funcionário.
            setor (str): Setor onde o funcionário trabalha.
            cargo (str): Cargo/posição do funcionário na empresa.
        """
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        """
        Gera uma apresentação formatada do funcionário.
        
        Returns:
            str: String formatada com a apresentação do funcionário,
                 incluindo nome, cargo e setor.
        """
        return f":handshake: Olá, meu nome é [blue]{self.nome}[/] e sou {self.cargo} e sou do setor de {self.setor} da empresa Curso em Vídeo."

funcionario1 = Funcionario("Leonardo", "TI", "Engenheiro de Software")
print(funcionario1.apresentacao())

funcionario2 = Funcionario("Bruna", "Psicologia", "Psicóloga")
print(funcionario2.apresentacao())
