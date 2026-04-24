from rich import print
from rich.panel import Panel
from abc import ABC, abstractmethod

class Funcionario(ABC):
    """Representa a base comum para os tipos de funcionarios do sistema."""

    salario_minimo = 1612
    inss = 7.5

    def __init__(self, nome, salario_bruto):
        """Inicializa os dados basicos do funcionario."""
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario_liquido = 0

    @abstractmethod
    def calcular_salario_liquido(self):
        """Calcula o salario liquido conforme a regra da classe filha."""
        pass

    def analisar_salario(self):
        """Exibe uma analise do salario liquido em relacao ao salario minimo."""
        texto_panel = (f"O salário de [blue]{self.nome}[/] ({f"[purple]{type(self).__name__}[/]"}) "
                       f"é de [green]R${self.salario_liquido:.2f}[/] e corresponde a "
                       f"[yellow]{self.salario_liquido / self.salario_minimo:.1f} salários mínimos.[/]")

        print(Panel(texto_panel, title="Análise Salarial", width=48))

class FuncionarioHorista(Funcionario):
    """Representa um funcionario remunerado por horas trabalhadas."""

    def __init__(self, nome,horas_trabalhadas, valor_hora):
        """Define nome, horas trabalhadas e valor recebido por hora."""
        super().__init__(nome, salario_bruto=0)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario_liquido(self):
        """Calcula o salario liquido com base nas horas e no desconto do INSS."""
        salario_bruto = self.valor_hora * self.horas_trabalhadas
        desconto_inss = salario_bruto * (self.inss / 100)
        self.salario_liquido = salario_bruto - desconto_inss

class FuncionarioMensalista(Funcionario):
    """Representa um funcionario com salario fixo mensal."""

    def __init__(self, nome, salario_mensal):
        """Define nome e valor do salario mensal do funcionario."""
        super().__init__(nome, salario_bruto=salario_mensal)
        self.salario_mensal = salario_mensal

    def calcular_salario_liquido(self):
        """Calcula o salario liquido aplicando o desconto do INSS."""
        desconto_inss = self.salario_mensal * (self.inss / 100)
        self.salario_liquido = self.salario_mensal - desconto_inss
