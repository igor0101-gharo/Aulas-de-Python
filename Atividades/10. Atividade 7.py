import os
os. system("cls")

idade = int (input("Digite sua idade:\n"))

if idade < 18 or idade > 65:
    print("você não é obrigado a votar.")
else:
    print("Você é obrigado a votar.")