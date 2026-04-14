from classe_pessoa import Pessoa

class Aluno(Pessoa):
    """Classe que representa um aluno, herdando de Pessoa."""

    def __init__(self, nome, idade, curso, turma):
        """Inicializa um aluno com nome, idade, curso e turma."""
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        """Realiza a matrícula do aluno no curso e turma especificados."""
        print(f"{self.nome} se matriculou no curso de '{self.curso}' na turma {self.turma}")