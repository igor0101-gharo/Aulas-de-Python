import os
os.system("cls")

soma = 0
for i in range(1,4):
    while True:
        nota = float(input(f"Digite sua {i}ª nota"))
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            break

media = soma/3

if media >= 7:
    print(f"Aprovado.\n Média:{media}")
elif media <= 6.9 and media > 5:
    print(f"Recuperação.\nMédia:{media}")
else:
    print(f"Reprovado.\nMédia:{media}")

