from classes import Aluno, Professor, Funcionario

def main():
    """Função principal para criar e demonstrar instâncias das classes Aluno, Professor e Funcionario."""
    aluno1 = Aluno("Leonardo", 20, "Engenharia de Software", "Turma A")
    aluno1.fazer_aniversario()
    aluno1.fazer_matricula()
    aluno1.estudar()
    #inspect(aluno1, methods=True)

    professor1 = Professor("Guanabara", 50, "Tecnologia", "Mestrado")
    professor1.fazer_aniversario()
    professor1.dar_aula()
    professor1.estudar()
    #inspect(professor1, methods=True)

    funcionaria1 = Funcionario("Mariana", 36, "Professora", "Secretaria")
    funcionaria1.fazer_aniversario()
    funcionaria1.bater_ponto()
    funcionaria1.estudar()
    #inspect(funcionaria1, methods=True)


if __name__ == "__main__":
    main()