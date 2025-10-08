import os
os.system("cls")

def media(nota):
    return sum(nota)/3
def mostrar_resultado(resultado):
    print(f"Sua média foi de {resultado:.2f}")
notas = []
for i in range(3):
    numero = float(input(f"Digite a {i+1}ª nota:\n "))
    notas.append(numero)
    os.system("cls")

resultado = media(notas)

mostrar_resultado(resultado)
