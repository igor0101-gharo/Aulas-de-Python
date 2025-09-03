import os
os.system("cls")

nota1 = float (input("Digite a primeira nota.\n"))
nota2 = float (input("Digite a segunda nota.\n"))
nota3 = float (input("Digite a terceira nota.\n"))
media = (nota1+nota2+nota3)/3

if media < 7:
    print(f"Sua média foi {media}\nVocê foi reprovado.")
else:
    print(f"Sua média foi {media}\nVocê foi aprovado.")