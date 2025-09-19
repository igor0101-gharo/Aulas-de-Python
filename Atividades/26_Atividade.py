import os
os.system("cls")


contador_pares = 0
contador_impares = 0
resto = 0
soma_pares =0
soma = 0
while True:
    numero = int(input("Digite um número."))
    resto = numero%2
    if numero == 0:
        break
    soma += numero
    if resto == 0:
        contador_pares += 1
        soma_pares += numero
    else:
        contador_impares +=1

total = contador_impares+contador_pares
media = soma/total
media_pares = soma_pares/contador_pares

print(f"Quantidade de pares digitados(contando o zero):{contador_pares+1}")
print(f"Quantidade de ímpares digitados:{contador_impares}")
print(f"Média dos valores pares(excluindo o zero):{media_pares}")
print(f"Média de todos os números(excluindo o zero):{media}")


        
