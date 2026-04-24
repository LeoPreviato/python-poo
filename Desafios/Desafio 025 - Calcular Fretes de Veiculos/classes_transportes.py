from abc import ABC, abstractmethod

class Transporte(ABC):
    """
    Classe abstrata que define a interface para diferentes tipos de transporte e cálculo de fretes.

    Atributos:
        distancia_frete (float): Distância em quilômetros para o frete.
        frete_por_km (float): Valor do frete calculado por quilômetro.
    """
    def __init__(self, distancia_frete):
        """
        Inicializa um transporte com a distância do frete.

        Args:
            distancia_frete (float): Distância em km para o frete.
        """
        self.distancia_frete = distancia_frete
        self.frete_por_km = distancia_frete * self.fator

    @abstractmethod
    def calcular_frete(self):
        """
        Método abstrato para calcular o frete.
        Deve ser implementado pelas subclasses.
        """
        pass

class Moto(Transporte):
    """
    Classe que representa uma motocicleta para transporte de carga.

    Atributos:
        fator (float): Multiplicador do frete por km (0.50).
    """
    fator = 0.50

    def calcular_frete(self):
        """
        Calcula o valor do frete para a motocicleta.

        Returns:
            str: O valor do frete formatado em reais.
        """
        return f"R${self.frete_por_km:.2f}"

class Caminhao(Transporte):
    """
    Classe que representa um caminhão para transporte de carga.

    Atributos:
        fator (float): Multiplicador do frete por km (1.50).
    """
    fator = 1.50

    def calcular_frete(self):
        """
        Calcula o valor do frete para o caminhão.
        O caminhão só aceita viagens com distância mínima de 50km.

        Returns:
            str: O valor do frete formatado em reais ou mensagem de erro se a distância for menor que 50km.
        """
        if self.distancia_frete < 50:
            return "[red]O caminhão não faz viagens com menos de 50km.[/]"
        return f"R${self.frete_por_km:.2f}"

class Drone(Transporte):
    """
    Classe que representa um drone para transporte de carga.

    Atributos:
        fator (float): Multiplicador do frete por km (9.50).
    """
    fator = 9.50

    def calcular_frete(self):
        """
        Calcula o valor do frete para o drone.
        O drone só aceita viagens com distância máxima de 10km.

        Returns:
            str: O valor do frete formatado em reais ou mensagem de erro se a distância for maior que 10km.
        """
        if self.distancia_frete > 10:
            return "[red]O drone não faz viagens com mais de 10km.[/]"
        return f"R${self.frete_por_km:.2f}"
