from rich import inspect

class Pessoa:
    """Classe que representa uma pessoa com nome e idade."""
    def __init__(self, nome = "", idade = 0):
        """Inicializa uma pessoa com nome e idade."""
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        """Incrementa a idade da pessoa em 1."""
        self.idade += 1


class Aluno(Pessoa):
    """Classe que representa um aluno, herdando de Pessoa, com curso e turma."""
    def __init__(self, nome, idade, curso, turma):
        """Inicializa um aluno com nome, idade, curso e turma."""
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        """Imprime mensagem de matrícula do aluno."""
        print(f"{self.nome} se matriculou no curso de '{self.curso}' na turma {self.turma}")

class Professor(Pessoa):
    """Classe que representa um professor, herdando de Pessoa, com especialidade e nível."""
    def __init__(self, nome, idade, especialidade, nivel):
        """Inicializa um professor com nome, idade, especialidade e nível."""
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        """Imprime mensagem de início de aula pelo professor."""
        print(f"O professor {self.nome}, iniciou a aula de '{self.especialidade}' com o nível '{self.nivel}")

class Funcionario(Pessoa):
    """Classe que representa um funcionário, herdando de Pessoa, com cargo e setor."""
    def __init__(self, nome, idade, cargo, setor):
        """Inicializa um funcionário com nome, idade, cargo e setor."""
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        """Imprime mensagem de batida de ponto pelo funcionário."""
        print(f"{self.nome} bateu o ponto no setor '{self.setor}' como '{self.cargo}'")

aluno1 = Aluno("Leonardo", 20, "Engenharia de Software", "Turma A")
aluno1.fazer_aniversario()
aluno1.fazer_matricula()
inspect(aluno1, methods=True)

professor1 = Professor("Guanabara", 50, "Tecnologia", "Mestrado")
professor1.fazer_aniversario()
professor1.dar_aula()
inspect(professor1, methods=True)

funcionaria1 = Funcionario("Mariana", 36, "Professora", "Secretaria")
funcionaria1.fazer_aniversario()
funcionaria1.bater_ponto()
inspect(funcionaria1, methods=True)