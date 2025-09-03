import os
os.system("cls")

nome = input("Digite o nome do Aluno:\n")
nota1 = float (input("Digite a primeira nota.\n"))
nota2 = float (input("Digite a segunda nota.\n"))
media = (nota1+nota2)/2

if media < 4:
    conceito = "E"
elif media < 6:
    conceito = "D"
elif media < 7.5:
    conceito = "C"
elif media < 9:
    conceito = "B"
elif media <= 10:
    conceito = "A"
else:
    conceito = "Valor inválido"

if media < 6:
    print(f"{nome}, você foi reprovado, seu conceito foi {conceito}.")
elif media <= 10:
    print(f"{nome}, você foi aprovado, seu conceito foi {conceito}.")
else:
    print(f"Média maior que o limite, você não digitou um valor válido.")
