import os
os.system("cls")

while True:
    nota1 = float(input("Qual a primeira nota?\n"))
    nota2 = float(input("Qual a segunda nota?\n"))
    if nota1 >= 0 and nota1 <= 10 and nota2 >= 0 and nota2 <=10:
        break

media = (nota1+nota2)/2

print(f"Média:{media}")