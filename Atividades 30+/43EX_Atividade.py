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
    while True:
        numero = float(input(f"Digite a {i+1}ª nota: \n"))
        if numero >=0 and numero <=10:
            notas.append(numero)
            os.system("cls")
            break
        else:
            input("Valor de nota inválido. A nota deve estar entre 0 e 10. Digite qualquer coisa para continuar")
            os.system("cls")

mostrar_resultado(notas)