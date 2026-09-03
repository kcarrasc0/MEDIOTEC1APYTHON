# DDESAFIO BIBLIOTECA

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir(self):
            print(f"Título: {self.titulo}")
            print(f"Autor: {self.autor}")
            print(f"Ano: {self.ano}")
            print("-" * 30)


# CADASTRO DO LIVRO

livros = [] #ARMAZENAR LIVROS

def cadastrar_livro():
    print("\n=== CADASTRAR LIVRO ===")

    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = input("Digite o ano de publicação do livro: ")

    livro = Livro(titulo, autor, ano)
    livros.append(livro)

    print("\nLivro cadastrado com sucesso!")

# LISTAGEM DE LIVROS 

def listar_livros():
    print("\n=== LISTA DE LIVROS ===")
    for livro in livros:
        livro.exibir()

# BUSCAR LIVROS

def buscar_livro():
    print("\n=== BUSCAR LIVRO ===")
    busca = input("Digite o título do livro que deseja buscar: ")

    encontrado = False

    for livro in livros:
        if busca.lower() in livro.titulo.lower():
            livro.exibir()
            encontrado = True

    if encontrado == False:
        print("Livro não encontrado.")

# QUANTIDADE DE LIVROS

def quantidade_livros():
    print("\n=== QUANTIDADE DE LIVROS ===")
    print(f"Quantidade de livros cadastrados: {len(livros)}")

# MENU DE OPÇÕES

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Buscar livro")
        print("4. Quantidade de livros")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            listar_livros()
        elif opcao == "3":
            buscar_livro()
        elif opcao == "4":
            quantidade_livros()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()