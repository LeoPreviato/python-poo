from abc import ABC, abstractmethod

class Pessoa(ABC):
    """Classe abstrata que representa uma pessoa."""

    def __init__(self, nome = "", idade = 0):
        """Inicializa uma pessoa com nome e idade."""
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        """Incrementa a idade da pessoa em 1 ano."""
        self.idade += 1

    @abstractmethod
    def estudar(self):
        """Método abstrato para estudar. Deve ser implementado pelas subclasses."""
        pass

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

    def estudar(self):
        """Imprime que o aluno está estudando o curso na turma."""
        print(f"O aluno {self.nome} está estudando '{self.curso}' na turma '{self.turma}")


class Professor(Pessoa):
    """Classe que representa um professor, herdando de Pessoa."""

    def __init__(self, nome, idade, especialidade, nivel):
        """Inicializa um professor com nome, idade, especialidade e nível."""
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        """Inicia uma aula do professor na especialidade e nível especificados."""
        print(f"O professor {self.nome}, iniciou a aula de '{self.especialidade}' com o nível '{self.nivel}'")

    def estudar(self):
        """Imprime que o professor é especialista na especialidade e nível."""
        print(f"{self.nome} é specialista em '{self.especialidade}' no nível '{self.nivel}'")


class Funcionario(Pessoa):
    """Classe que representa um funcionário, herdando de Pessoa."""

    def __init__(self, nome, idade, cargo, setor):
        """Inicializa um funcionário com nome, idade, cargo e setor."""
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        """Registra o ponto do funcionário no setor e cargo especificados."""
        print(f"{self.nome} bateu o ponto no setor '{self.setor}' como '{self.cargo}'")

    def estudar(self):
        """Imprime que o funcionário está se especializando para o cargo."""
        print(f"{self.nome} está se especializando para o cargo de '{self.cargo}'")
