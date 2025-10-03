import os



def logo_senai():
    print("=========")
    print("= SENAI =") 
    print("=========")

os.system("cls")
logo_senai()
nome = input("Digite seu nome: ")

os.system("cls")
logo_senai()
idade = int(input("Digite sua idade: "))

os.system("cls")
logo_senai()
peso = float(input("Digite seu peso: "))

os.system("cls")
logo_senai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")