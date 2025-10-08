import os
os.system("cls")

# Definindo as funções
def somar(n1 , n2):
    return n1+ n2

def subtrair(n1 , n2):
    return n1 - n2

def multiplicar(n1,n2):
    return n1 * n2 

def dividir(n1,n2):
    return n1/n2 if n2 != 0 else "Divisão por zero"

#Solicitando os dados do usuário
primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

#Utilizando as funções para colocar valores nas variáveis
soma = somar(primeiro_numero , segundo_numero)
subtracao = subtrair(primeiro_numero, segundo_numero)
multiplicacao = multiplicar(primeiro_numero, segundo_numero)
divisao = dividir(primeiro_numero, segundo_numero)

#Mostrando o resultado
print(f"Soma:{soma}")
print(f"Subtração: {subtracao} ")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

