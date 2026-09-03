# SISTEMA DE CADASTRO DE ALUNOS
# Revisão geral da Trilha de Python


# MÓDULO 6 e 7 — CLASSES, OBJETOS E MÉTODOS

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos.")


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, nota):
        super().__init__(nome, idade)
        self.curso = curso
        self.nota = nota

    def verificar_situacao(self):
        if self.nota >= 7:
            return "Aprovado"
        elif self.nota >= 5:
            return "Recuperação"
        else:
            return "Reprovado"

    def apresentar(self):
        print(f"\nAluno: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Curso: {self.curso}")
        print(f"Nota: {self.nota:.1f}")
        print(f"Situação: {self.verificar_situacao()}")


class Monitor(Aluno):
    def __init__(self, nome, idade, curso, nota, horas_monitoria):
        super().__init__(nome, idade, curso, nota)
        self.horas_monitoria = horas_monitoria

    def apresentar(self):
        super().apresentar()
        print(f"Horas de monitoria: {self.horas_monitoria}")


# MÓDULO 1 — VARIÁVEIS E TIPOS DE DADOS

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade: "))
curso = input("Digite o curso: ")
nota = float(input("Digite a nota: "))


# MÓDULO 2 — OPERADORES E ATRIBUIÇÃO

nota += 0  # exemplo de atribuição composta

print("\nCadastro realizado!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Curso: {curso}")
print(f"Nota: {nota:.1f}")


# MÓDULO 3 — CONDICIONAIS

if idade >= 18 and nota >= 7:
    print("Aluno maior de idade e aprovado.")
elif idade >= 18 and nota >= 5:
    print("Aluno maior de idade e em recuperação.")
elif idade < 18 or nota < 5:
    print("Aluno menor de idade ou com nota abaixo da média.")


# MÓDULO 6 — CRIANDO UM OBJETO

aluno = Aluno(nome, idade, curso, nota)

aluno.apresentar()


# MÓDULO 8 — HERANÇA E POLIMORFISMO

monitor = Monitor(
    "Maria",
    20,
    "Desenvolvimento de Sistemas",
    9.0,
    10
)

monitor.apresentar()


# MÓDULO 4 — WHILE E MENU INTERATIVO

alunos = [aluno, monitor]

while True:

    print("\n========== MENU ==========")
    print("1 - Listar alunos")
    print("2 - Cadastrar aluno")
    print("3 - Ver aprovados")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        # ----------------------------------
        # MÓDULO 5 — FOR E RANGE

        print("\n--- ALUNOS CADASTRADOS ---")

        for i in range(len(alunos)):
            print(f"\nAluno {i + 1}")
            alunos[i].apresentar()

    elif opcao == "2":

        nome = input("\nNome: ")
        idade = int(input("Idade: "))
        curso = input("Curso: ")
        nota = float(input("Nota: "))

        novo_aluno = Aluno(nome, idade, curso, nota)

        alunos.append(novo_aluno)

        print("\nAluno cadastrado com sucesso!")

    elif opcao == "3":

        print("\n--- ALUNOS APROVADOS ---")

        encontrou = False

        for aluno in alunos:

            if aluno.verificar_situacao() == "Aprovado":
                print(f"- {aluno.nome}")
                encontrou = True

        if not encontrou:
            print("Nenhum aluno aprovado.")

    elif opcao == "4":

        print("\nEncerrando o sistema...")
        break

    else:

        print("\nOpção inválida!")
        continue


print("\nPrograma finalizado!")