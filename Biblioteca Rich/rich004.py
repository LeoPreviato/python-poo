from rich import print
from rich import inspect

from Exercicios.ex003.ex003 import conta1


class ContaBancaria:
    """
    Crie uma conta bancária que permite realizar saques e depositos
    """
    def __init__(self, id, nome, saldo):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual: R${self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado com sucesso na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque NEGADO para o valor de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado com sucesso na conta {self.id}")

conta = ContaBancaria(1, "Leonardo", 1000)

inspect(conta)