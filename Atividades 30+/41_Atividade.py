import os
os.system("cls")

def aumento(preco):
    if preco < 100:
        return preco * 1.10
    else:
        return preco * 1.20

def mostrar_resultado(resultado):
    print(f"O valor acrescido de juros é de R${resultado:.2f}")
preco = float(input("Digite o valor:\nR$"))
novo_preco = aumento(preco)
mostrar_resultado(novo_preco)