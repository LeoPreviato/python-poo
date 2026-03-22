# Declaração de Classes
class Gafanhoto:
    """Classe Gafanhoto: Representa uma pessoa com nome e idade.
    para criar uma nova pessoa, basta passar o nome e a idade como argumentos.
    Exemplo: variavel = Gafanhoto("Nome", Idade)"""

    def __init__(self, nome = "", idade = 0): # Método construtor
        self.nome = nome
        self.idade = idade

    # Método de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Declaração de Objetos
gafanhoto1 = Gafanhoto("Leonardo", 20)
gafanhoto1.aniversario()
#print(gafanhoto1)
print(gafanhoto1.__dict__) # Attribute
print(gafanhoto1.__getstate__()) # Method
print(gafanhoto1.__class__)
print(gafanhoto1.__doc__) #Dunder Attribute

