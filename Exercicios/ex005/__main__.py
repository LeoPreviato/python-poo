from rich import inspect
from classes_ex005 import Aluno, Professor, Funcionario

def main():
    aluno1 = Aluno("Leonardo", 20, "Engenharia de Software", "Turma A")
    aluno1.fazer_aniversario()
    aluno1.fazer_matricula()
    #inspect(aluno1, methods=True)

    professor1 = Professor("Guanabara", 50, "Tecnologia", "Mestrado")
    professor1.fazer_aniversario()
    professor1.dar_aula()
    #inspect(professor1, methods=True)

    funcionaria1 = Funcionario("Mariana", 36, "Professora", "Secretaria")
    funcionaria1.fazer_aniversario()
    funcionaria1.bater_ponto()
    #inspect(funcionaria1, methods=True)

if __name__ == "__main__":
    main()