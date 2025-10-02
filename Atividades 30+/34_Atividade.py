import os 
os.system("cls")

negativos =[]
positivos =[]

quantidade = 5

for i in range(quantidade):
    numeros = float(input(f"Digite o {i+1}º número:\n"))
    if numeros < 0:
        negativos.append(numeros)
    else:
        positivos.append(numeros)

print(f"Quantidade de números negativos: {len(negativos)}")
print(f"Soma dos números positivos: {sum(positivos)}")