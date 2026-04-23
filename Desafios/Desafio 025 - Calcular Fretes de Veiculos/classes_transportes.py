from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia_frete):
        self.distancia_frete = distancia_frete
        self.frete_por_km = distancia_frete * self.fator

    @abstractmethod
    def calcular_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50

    def calcular_frete(self):
        return f"R${self.frete_por_km:.2f}"

class Caminhao(Transporte):
    fator = 1.50

    def calcular_frete(self):
        if self.distancia_frete < 50:
            return "[red]O caminhão não faz viagens com menos de 50km.[/]"
        return f"R${self.frete_por_km:.2f}"

class Drone(Transporte):
    fator = 9.50

    def calcular_frete(self):
        if self.distancia_frete > 10:
            return "[red]O drone não faz viagens com mais de 10km.[/]"
        return f"R${self.frete_por_km:.2f}"
