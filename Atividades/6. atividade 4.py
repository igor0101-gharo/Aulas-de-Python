import os
os.system("cls")

nome = input("Digite seu nome:\n")
idade = int(input("Digite sua idade:\n"))
if idade < 16:
    print(f"Você não pode votar, {nome}")
elif idade <= 17:
    print(f"Seu voto é opcional, {nome}")
elif idade < 65:
    print(f"Seu voto é obrigátorio, {nome}")
else:
    print(f"Você não é obrigado a votar, {nome}")

print("FIM")
