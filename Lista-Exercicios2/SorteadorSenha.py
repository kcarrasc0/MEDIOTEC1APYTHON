# Sorteador de Senha Simples

import random

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

quantidade = int(input("Quantos caracteres a senha deve ter? "))

senha = ""

for i in range(quantidade):
    senha += random.choice(caracteres)

print(f"\nSenha gerada: {senha}")