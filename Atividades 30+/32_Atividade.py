import os
os.system("cls")

numeros =[]
quantidade = 6
par = 0
impar = 0
for i in range(quantidade):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
    if numero%2 == 0:
        par += 1
    else:
        impar +=1

for i in range(quantidade):
    print(f"{i+1}º número digitado: {numeros[i]}")
print(f"Quantidade de pares: {par}")
print(f"Quantidade de ímpares: {impar} ")

    

