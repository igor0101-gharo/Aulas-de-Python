import os
os.system("cls")

contador = 0
soma = 0
while True:
    numero = int(input("Digite um número positivo.\nSe quiser saber a média, digite um número negativo "))
    if numero >= 0:
        soma += numero
        contador += 1
    elif numero < 0:
        break

media = soma/contador

print(f"A média dos números digitados foi:{media}")