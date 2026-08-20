# SISTEMA DE PERSONAGENS


class Personagem:

    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def mostrar_informacoes(self):
        print(f"""
Nome: {self.nome}
Vida: {self.vida}
Ataque: {self.ataque}
""")

    def atacar(self, outro_personagem):
        outro_personagem.vida -= self.ataque

        print(
            f"{self.nome} atacou "
            f"{outro_personagem.nome}!"
        )

        print(
            f"{outro_personagem.nome} "
            f"perdeu {self.ataque} de vida."
        )


# Herança com tipo mago

class Mago(Personagem):

    def __init__(self, nome, vida, ataque, magia):
        super().__init__(nome, vida, ataque)
        self.magia = magia

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Magia: {self.magia}")


# Criar personagem


def criar_personagem():

    print("\n=== CRIAR PERSONAGEM ===")

    nome = input("Nome: ")

    vida = int(input("Vida: "))

    ataque = int(input("Ataque: "))

    tipo = input(
        "É um mago? (s/n): "
    ).lower()

    if tipo == "s":

        magia = input("Nome da magia: ")

        personagem = Mago(
            nome,
            vida,
            ataque,
            magia
        )

    else:

        personagem = Personagem(
            nome,
            vida,
            ataque
        )

    print("\nPersonagem criado!")

    return personagem


# Programa Principal de Personagens


personagens = []

contador = 0


print("================================")
print("     SISTEMA DE PERSONAGENS")
print("================================")


while True:

    print("\n===== MENU =====")

    print("1 - Criar personagem")
    print("2 - Listar personagens")
    print("3 - Batalhar")
    print("4 - Sair")

    opcao = input("Escolha: ")

    # Contador
    contador += 1

# Criando

    if opcao == "1":

        personagem = criar_personagem()

        personagens.append(personagem)

   # Lista

    elif opcao == "2":

        if len(personagens) == 0:

            print("\nNenhum personagem cadastrado.")

        else:

            print("\n=== PERSONAGENS ===")

            for i in range(len(personagens)):

                print(f"\nPersonagem {i + 1}")

                personagens[i].mostrar_informacoes()

  # Batalha de personagens

    elif opcao == "3":

        if len(personagens) < 2:

            print(
                "\nVocê precisa de pelo menos "
                "2 personagens."
            )

            continue

        print("\nEscolha os personagens:")

        for i in range(len(personagens)):

            print(
                f"{i + 1} - "
                f"{personagens[i].nome}"
            )

        personagem1 = int(
            input("Primeiro personagem: ")
        )

        personagem2 = int(
            input("Segundo personagem: ")
        )

        if personagem1 == personagem2:

            print(
                "\nVocê não pode batalhar "
                "contra você mesmo!"
            )

        elif (
            personagem1 < 1
            or personagem1 > len(personagens)
            or personagem2 < 1
            or personagem2 > len(personagens)
        ):

            print("\nPersonagem inválido!")

        else:

            jogador1 = personagens[personagem1 - 1]
            jogador2 = personagens[personagem2 - 1]

            jogador1.atacar(jogador2)

            if jogador2.vida <= 0:

                print(
                    f"\n{jogador2.nome} "
                    "foi derrotado!"
                )

            else:

                print(
                    f"\n{jogador2.nome} "
                    f"ainda possui "
                    f"{jogador2.vida} de vida."
                )

  # Vazando LogOut

    elif opcao == "4":

        print("\nSistema encerrado!")

        print(
            f"Total de operações: {contador}"
        )

        break

    else:

        print("\nOpção inválida!")

        continue