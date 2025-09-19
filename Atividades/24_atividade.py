import os
os.system("cls")

nota = 0
contador = 0
soma = 0
error = "sim"
while True:
    continuar = input("Deseja digitar mais uma nota?(S ou N)").upper()
    match continuar:
        case "S":
            nota = float(input("Digite a nota:\n"))
            if nota >=0 and nota <= 10:
                contador += 1
                soma = soma + nota
                os.system("cls")
            else:
                print("Valor de nota inválido.")
                error = input("Digite qualquer coisa para retornar.")
                os.system("cls")
        case "N":
            media = soma/contador
            break 
        case _:
            print("Opção inválida.")
            error = input("Digite qualquer coisa para retornar.")
            os.system("cls")

print(f"O total das notas é {soma:.2f}.")
print (f"A média das notas informadas é {media:.2f}.")
