class Pessoa:
    """Classe base que representa uma pessoa."""

    def __init__(self, nome = "", idade = 0):
        """Inicializa uma pessoa com nome e idade."""
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        """Incrementa a idade da pessoa em 1 ano."""
        self.idade += 1