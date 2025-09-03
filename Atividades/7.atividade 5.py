import os
os.system("cls")
import math

n1 = float (input("Digite um número"))
n2 = float (input("Digite outro número"))
distancia= (n1-n2)**2

modulo = math.sqrt(distancia)
maior = (n1+n2)/2 + modulo/2

print(f"{maior} é o maior.")