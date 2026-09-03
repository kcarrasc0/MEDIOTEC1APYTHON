class Aluno: 
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        print(f"Salve meu nome é {self.nome}.")
        print(f"Tenho {self.idade} anos.")
        print(f"Estou estudando {self.curso}.")

print("----- Cadastro do Aluno 1 ------")

nomeAluno1 = input("Digite o nome do Aluno1:")
idadeAluno1 = int(input("Digite a idade do Aluno1:"))
cursoAluno1 = input("Digite o curso do Aluno1:")

aluno1 = Aluno (nomeAluno1, idadeAluno1, cursoAluno1)

print("----- Cadastro do Aluno 2 ------")

nomeAluno2 = input("Digite o nome do Aluno2:")
idadeAluno2 = int(input("Digite a idade do Aluno2:"))
cursoAluno2 = input("Digite o curso do Aluno2:")

aluno2 = Aluno (nomeAluno2, idadeAluno2, cursoAluno2)

aluno1.apresentar()
print()
aluno2.apresentar()