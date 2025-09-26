import os
os.system("cls")

contador_familia = 0
total_filhos = 0
maior_salario = 0
menor_salario = 99999999999999999999
total_salario = 0
while True:
    print("""
Código| Descrição
    1 | Adicionar família
    2 | Sair e exibir resultados""")
    codigo = int(input("Digite a ação desejada.\n"))
    match codigo:
        case 1:
            contador_familia += 1 
            filhos = int(input("Digite o número de filhos da família.\n"))
            total_filhos += filhos
            salario = float(input("Digite o salário de sua família.\nR$"))
            total_salario += salario
            if salario > maior_salario:
                maior_salario = salario
            if salario < menor_salario:
                menor_salario = salario
            os.system("cls")
        case 2:
            media_filhos = total_filhos/contador_familia if contador_familia != 0 else 0
            media_salario = total_salario/contador_familia if contador_familia != 0 else 0

            print(f"Número de famílias: {contador_familia}")
            print(f"Média de salários: R${media_salario:.2f}")
            print(f"Média do número de filhos: {media_filhos}")
            print(f"Maior salário: R${maior_salario:.2f}")
            print(f"Menor salário: R${menor_salario:.2f}")
            break
