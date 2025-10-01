import os
os.system("cls")

lista_numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    lista_numeros.append(numero)

maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)
print("\n")
for i in range(5):
    print(f"{i+1}º número: {lista_numeros[i]}\n")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Menor número: {min(lista_numeros)}")