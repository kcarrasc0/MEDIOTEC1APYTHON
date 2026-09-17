# Caixa Eletrônico

saldo = 1000.00

while True:
    print("\n===== CAIXA ELETRÔNICO =====")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "2":
        valor = float(input("Valor do depósito: R$ "))
        saldo += valor
        print("Depósito realizado com sucesso!")

    elif opcao == "3":
        valor = float(input("Valor do saque: R$ "))

        if valor <= saldo:
            saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")

    elif opcao == "4":
        print("Obrigado por utilizar o sistema.")
        break

    else:
        print("Opção inválida.")