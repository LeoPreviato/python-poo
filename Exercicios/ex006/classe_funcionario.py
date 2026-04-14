from classe_pessoa import Pessoa

class Funcionario(Pessoa):
    """Classe que representa um funcionário, herdando de Pessoa."""

    def __init__(self, nome, idade, cargo, setor):
        """Inicializa um funcionário com nome, idade, cargo e setor."""
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        """Registra o ponto do funcionário no setor e cargo especificados.

        Este método imprime uma mensagem indicando o nome do funcionário, o setor
        e o cargo em que o ponto foi batido.
        """
        print(f"{self.nome} bateu o ponto no setor '{self.setor}' como '{self.cargo}'")