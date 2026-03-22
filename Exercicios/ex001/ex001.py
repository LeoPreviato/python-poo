# Declaração de Classes
class Gafanhoto:
    def __init__(self): # Método construtor
        self.nome = ""
        self.idade = 0

    # Método de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos."

# Declaração de Objetos
gafanhoto1 = Gafanhoto()
gafanhoto1.nome = "Leonardo"
gafanhoto1.idade = 20
gafanhoto1.aniversario()
print(gafanhoto1.mensagem())

gafanhoto2 = Gafanhoto()
gafanhoto2.nome = "Bruna"
gafanhoto2.idade = 19
gafanhoto2.aniversario()
print(gafanhoto2.mensagem())

gafanhoto3 = Gafanhoto()
print(gafanhoto3.mensagem())