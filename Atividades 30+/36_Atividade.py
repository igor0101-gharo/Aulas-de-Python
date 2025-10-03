import os
os.system("cls")

def par_impar(numero):
    if numero%2 == 0:
        print("O número é par")
    else:
        print("O número é impar")

numero = float(input("Digite um número:\n"))

par_impar(numero)