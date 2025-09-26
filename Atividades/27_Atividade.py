import os 
os.system("cls")

contador_M = 0
contador_F = 0
maior_idade = 0
menor_idade = 99999999
soma = 0
alto_salario = 0
total = 0
while True:
    print("""
Código| Descrição
    1 | Adicionar pessoa
    2 | Exibir resultados
    3 | Sair""")
    codigo = int(input("Digite a ação desejada.\n"))
    match codigo:
        case 1:
            idade = int(input("Digite a idade.\n"))
            if idade > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade
            sexo = input("Digite o sexo (M ou F)\n").upper()
            if sexo == "M":
                contador_M +=1
            elif sexo == "F":
                contador_F +=1
            salario = float(input("Digite o salário.\n"))
            soma += salario
            if salario >= 5000 and sexo == "F":
                alto_salario += 1
            os.system("cls")
        case 2:
            total = contador_F + contador_M
            media = soma/total if total != 0 else 0
            print(f"Média de salário: {media:.2f}")
            print(f"Maior idade: {maior_idade}\nMenor idade: {menor_idade}")
            print(f"Quantidade de mulheres com salário alto: {alto_salario}")
            break
        case 3:
            os.system("cls")
            print("Aplicação encerrada.")
            break
            
        case _:
            print("Valor invalido.")
            error = input("Digite qualquer coisa para retornar.")
            os.system("cls")


            