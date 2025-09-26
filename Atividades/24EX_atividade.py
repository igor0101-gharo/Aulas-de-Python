import os
os.system("cls")

soma = 0
contador = 0
while True:
    continuar = input("Deseja inserir uma nota?\n.S\n.N").upper()
    if continuar =="S":
        nota = float(input("Digite sua nota:\n"))
        soma += nota
        contador += 1
    elif continuar == "N":
        break
    else:
        print("resposta inválida. Por favor digite S ou N")

media = soma/contador

print(f"Média das notas: {media:.2f}")
