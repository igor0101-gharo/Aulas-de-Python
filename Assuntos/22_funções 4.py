import os
os.system("cls")
import time

# função limpar a tela

def limpar():
    time.sleep(3)
    os.system("cls")

# Função com parâmetros e com retorno

def somar(n1,n2):
    return n1 + n2

# Função com parâmetros e sem retorno

def mostrar_resultado(soma):
    print(f"Resultado: {soma}")

limpar

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número:"))

soma = somar(primeiro_numero , segundo_numero)


mostrar_resultado(soma)
