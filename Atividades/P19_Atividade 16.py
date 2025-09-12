import os 
os.system("cls")

print("Laço de repetição - WHILE")

quantidade_notas = 2
soma = 0

for i in range(quantidade_notas):
    while True:
        nota = float(input(f"Digite a {i+1}ª nota:"))
        if nota >= 0 and nota <= 10:
            break
    soma = soma + nota

media = soma/quantidade_notas

print(f"Média: {media}")