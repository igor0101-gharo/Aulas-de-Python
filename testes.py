import os
os.system("cls")

numero1 = float (input("Digite seu número"))
numero2 = float (input("Digite o seugundo número"))

print(f"primeiro:{numero1}")
print(f"Segundo:{numero2}")

#divisões em python retornam um float. para ver apenas a parte inteira use o comando "//". O comando "%" retorna o resto da divisão

divisao = numero1/numero2
divisaointeira = numero1//numero2
resto= numero1%numero2

print(f"Divisão:{divisao}\nParte inteira:{divisaointeira}")
print(f"Resto da divisão:{resto}")
