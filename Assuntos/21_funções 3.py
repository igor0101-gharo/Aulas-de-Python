import os
os.system("cls")

# Criando a função:
def saudacao(nome, idade , altura , peso):
    print(f"Olá, {nome}!Bem-vindo(a)")
    print(f"Sua idade é {idade} anos")
    print(f"Sua altura é {altura} metros")
    print(f"Seu peso é {peso} kg")

print("-Solicitando dados-")
name = input("Digite seu nome:\n")
age = int(input("Digite sua idade:\n"))
height = float(input("Digite sua altura:\n"))
weight = float(input("Digite seu peso:\n"))

# Chamando a função:
saudacao(name, age, height, weight)


