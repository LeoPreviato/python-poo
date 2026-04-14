from classe_pessoa import Pessoa

class Professor(Pessoa):
    """Classe que representa um professor, herdando de Pessoa."""

    def __init__(self, nome, idade, especialidade, nivel):
        """Inicializa um professor com nome, idade, especialidade e nível."""
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        """Inicia uma aula do professor na especialidade e nível especificados."""
        print(f"O professor {self.nome}, iniciou a aula de '{self.especialidade}' com o nível '{self.nivel}")