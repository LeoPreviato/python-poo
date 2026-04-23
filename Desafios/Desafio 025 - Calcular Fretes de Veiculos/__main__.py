from classes_transportes import *
from rich import print

def main():
    distancia = 10

    entrega = Drone(distancia)
    print(f"Frete de {type(entrega).__name__} em {distancia}Km = {entrega.calcular_frete()}")

if __name__ == "__main__":
    main()