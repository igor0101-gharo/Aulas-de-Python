import os
os.system("cls")

def cm_para_m(metros):
    return metros*100

def mostrar_resultado(resultado):
    print(f"Resultado da conversão: {resultado} cm")
numero = float(input("Digite um número em metros para converter em centimetros:\n"))
resultado = cm_para_m(numero)

mostrar_resultado(resultado)