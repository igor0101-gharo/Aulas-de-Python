import os
os.system("cls")

while True:
    nota = float(input("Qual sua nota?\n"))
    if nota >= 0 and nota <= 10:
        break

print(f"Sua nota foi {nota:.2f}")
    