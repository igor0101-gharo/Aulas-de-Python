import os
os.system("cls")

lista_notas = []

for i in range(4):
    nota= float(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
media = soma/ len(lista_notas)

if media >= 7:
    for i in range(4):
        print(f"{i+1}ª nota:{lista_notas[i]}")
    print(f"Média: {media:.2f}")
    print("Resultado: Aprovado")
elif media >= 5:
    for i in range(4):
        print(f"{i+1}ª nota:{lista_notas[i]}")
    print(f"Média: {media:.2f}")
    print("Resultado: Recuperação")
elif media < 5:
    for i in range(4):
        print(f"{i+1}ª nota:{lista_notas[i]}")
    print(f"Média: {media:.2f}")
    print("Resultado: Reprovado")