from classes_funcionarios import *

def main():
    f1 = FuncionarioHorista("Leonardo", 12, 200)
    f1.calcular_salario_liquido()
    f1.analisar_salario()

    f2 = FuncionarioMensalista("Bruna", 9500)
    f2.calcular_salario_liquido()
    f2.analisar_salario()

if __name__ == '__main__':
    main()