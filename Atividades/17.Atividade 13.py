import os
os.system("cls")

altura = float (input("Digite Sua altura(em metros):\n"))
sexo = input("Digite seu sexo (digite 'M' para sexo masculino e 'F' para  sexo feminino).\n")

match sexo:
    case "M":
        print(f"O peso ideal para você é de {72.7*altura - 58:.2F}kg")
    case "F":
        print(f"O peso ideal para você é de {62.1*altura - 44.7:.2F}kg")
    case _:
        print("Sexo inválido")
