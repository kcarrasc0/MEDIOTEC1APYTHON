class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome}.")
        print(f"Tenho {self.idade} anos.")
        print(f"Estou estudando {self.curso}.")


# Recebendo os dados do primeiro aluno
print("=== Cadastro do Aluno 1 ===")

nome1 = input("Digite o nome: ")
idade1 = int(input("Digite a idade: "))
curso1 = input("Digite o curso: ")

# Criando o primeiro objeto
aluno1 = Aluno(nome1, idade1, curso1)


# Recebendo os dados do segundo aluno
print("\n=== Cadastro do Aluno 2 ===")

nome2 = input("Digite o nome: ")
idade2 = int(input("Digite a idade: "))
curso2 = input("Digite o curso: ")

# Criando o segundo objeto
aluno2 = Aluno(nome2, idade2, curso2)


# Utilizando o método
print("\n=== Dados dos Alunos ===")

aluno1.apresentar()

print()

aluno2.apresentar()