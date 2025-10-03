import os
os.system("cls")

def tabuada(numero):
    print(f"Tabuada do número {numero}")
    for i in range(10):
        print(f"{numero} x {i+1} = {numero * (i+1)}")

numero = int(input("Digite um número:\n"))

tabuada(numero)