# trabalhar init, self, def 



class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome}.")
        print(f"Tenho {self.idade} anos.")
        print(f"Estou estudando {self.curso}.")


# Criando objetos a partir da classe
aluno1 = Aluno("João", 20, "Python")
aluno2 = Aluno("Maria", 19, "JavaScript")

# Utilizando o método
aluno1.apresentar()
print()
aluno2.apresentar()