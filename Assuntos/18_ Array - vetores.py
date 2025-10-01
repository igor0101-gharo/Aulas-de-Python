import os 
os.system("cls")

lista_notas = []

for i in range(3):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)
    #soma += nota

soma = sum(lista_notas)
soma2 = sum(lista_notas[0] , lista_notas[1])




print(f"Nota: {lista_notas}")
#print(f"Nota: {lista_notas[0]}")
#print(f"Nota: {lista_notas[1]}")
#print(f"Nota: {lista_notas[2]}")

for i in range(3):
    print(f'Nota: {lista_notas[i]}')
print(f"Soma: {soma}")
print(f"Soma: {soma2}")

#print(f"Soma:{soma}")
print("FIM")