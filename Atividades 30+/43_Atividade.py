import os
os.system("cls")

def aprovar(media):
    print(f"Sua media é {media:.2f}. Você foi aprovado")

def reprovar(media):
    print(f"Sua media é {media:.2f}. Você foi reprovado")


def mostrar_resultado(nota):
    media = sum(nota)/2
    if media >= 7:
        aprovar(media)
    else:
        reprovar(media)


notas = []
for i in range(2):
    numero = float(input(f"Digite a {i+1}ª nota: \n"))
    notas.append(numero)
    os.system("cls")

mostrar_resultado(notas)