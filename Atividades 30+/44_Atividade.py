import os
os.system("cls")

def achar_idade(ano):
    return 2025 - ano
def mostrar_resultado(idade):
    print(f"Você tem {idade} anos")

ano = int(input("Digite o ano que você nasceu:\n"))

idade = achar_idade(ano)

mostrar_resultado(idade)
