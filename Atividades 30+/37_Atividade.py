import os
os.system("cls")

def positivo_negativo(numero):
    if numero >= 0:
        print(f"{numero} é um número positivo")
    else:
        print(f"{numero} é um número negativo")

numero = int(input("Digite um número intiero:\n"))

positivo_negativo(numero)