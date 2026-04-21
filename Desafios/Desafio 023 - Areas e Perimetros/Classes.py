from abc import ABC, abstractmethod

class Poligono(ABC):
    """Classe abstrata que representa um polígono."""

    def __init__(self, quantidade_lados):
        """Inicializa o polígono com a quantidade de lados."""
        self.quantidade_lados = quantidade_lados

    @abstractmethod
    def calcular_perimetro(self):
        """Calcula o perímetro do polígono. Deve ser implementado pelas subclasses."""
        pass

    @abstractmethod
    def calcular_area(self):
        """Calcula a área do polígono. Deve ser implementado pelas subclasses."""
        pass


class Quadrado(Poligono):
    """Classe que representa um quadrado, herda de Poligono."""

    def __init__(self, lado, quantidade_lados=4):
        """Inicializa o quadrado com o lado e quantidade de lados (padrão 4)."""
        super().__init__(quantidade_lados)
        self.lado = lado

    def calcular_perimetro(self):
        """Calcula o perímetro do quadrado."""
        return self.lado * self.quantidade_lados

    def calcular_area(self):
        """Calcula a área do quadrado."""
        return self.lado ** 2

class Circulo(Poligono):
    """Classe que representa um círculo, herda de Poligono."""

    def __init__(self, raio, quantidade_lados=0):
        """Inicializa o círculo com o raio e quantidade de lados (padrão 0)."""
        super().__init__(quantidade_lados)
        self.raio = raio

    def calcular_perimetro(self):
        """Calcula o perímetro (circunferência) do círculo."""
        return 2 * 3.14 * self.raio

    def calcular_area(self):
        """Calcula a área do círculo."""
        return 3.14 * self.raio ** 2