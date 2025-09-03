import os
os.system("cls")

numero1 = int(input("Digite o primeiro número\n"))
numero2 = int(input("Digite o segundo número\n"))

maior = max(numero1, numero2)
menor = min(numero1, numero2)

print (f"Média: {(numero1+numero2)/2}")
print (f'Soma: {numero1+numero2}')
print (f"Produto: {numero1*numero2} ")

if numero1>numero2:
    print(f"Maior valor: {numero1}\nMenor valor: {numero2}")
elif numero2>numero1:
    print(f"Maior valor: {numero2}\nMenor valor: {numero1}")
else:
    print("Os números são iguais.\nFIM")