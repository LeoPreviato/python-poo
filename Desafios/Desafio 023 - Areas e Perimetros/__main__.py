from rich import print
from Classes import *


def main():
    p1 = Quadrado(12)

    print(f"Perímetro: {p1.calcular_perimetro():.1f}")
    print(f"Área: {p1.calcular_area():.1f}")

if __name__ == "__main__":
    main()
