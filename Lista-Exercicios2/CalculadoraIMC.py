# Calculadora de IMC

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    situacao = "Abaixo do peso"
elif imc < 25:
    situacao = "Peso normal"
elif imc < 30:
    situacao = "Sobrepeso"
else:
    situacao = "Obesidade"

print("\n===== RESULTADO =====")
print(f"Nome: {nome}")
print(f"IMC: {imc:2f}")
print(f"Classificação: {situacao}")

# = recebe algo
# == estritamernte igual ao valor
# * multiplicação
# ** quadrado ou potencia