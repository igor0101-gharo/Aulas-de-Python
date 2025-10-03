import os
os.system("cls")


numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número:"))
    if numero < 0:
        numero = 0
    numeros.append(numero)

for i, numero in enumerate(numeros, start= 1):
    print(f"{i}º número: {numero}")

