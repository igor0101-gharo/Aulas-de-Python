import os
os.system("cls")

pratos = []
valores =[]
quantidade = 0

while True:
    print(""""
Código\t Prato\t\t Valor
  1\t Picanha\t R$25,00
  2\t Lasanha\t R$20,00
  3\t Strogonoff\t R$18,00
  4\t Bife Acebolado\t R$15,00
  5\t Pão com ovo\t R$5,00      
""")
    codigo = int(input("Digite o código de seu prato:\n"))
    match codigo:
        case 1:
            quantidade += 1
            pratos.append("Picanha")
            valores.append(25)
            parar = input("Digite 'S' para fazer outro pedido.(qualquer outro valor encerrará o pedido)" ).upper()
            if parar == "S":
                os.system("cls")
            else:
                break
        case 2:
            quantidade += 1
            pratos.append("Lasanha")
            valores.append(20)
            parar = input("Digite 'S' para fazer outro pedido.(qualquer outro valor encerrará o pedido)\n" ).upper()
            if parar == "S":
                os.system("cls")
            else:
                break
        case 3:
            quantidade += 1
            pratos.append("Strogonoff")
            valores.append(18)
            parar = input("Digite 'S' para fazer outro pedido.(qualquer outro valor encerrará o pedido)\n" ).upper()
            if parar == "S":
                os.system("cls")
            else:
                break
        case 4:
            quantidade += 1
            pratos.append("Bife Acebolado")
            valores.append(15)
            parar = input("Digite 'S' para fazer outro pedido.(qualquer outro valor encerrará o pedido)\n" ).upper()
            if parar == "S":
                os.system("cls")
            else:
                break
        case 5:
            quantidade += 1
            pratos.append("Pão com ovo")
            valores.append(5)
            parar = input("Digite 'S' para fazer outro pedido.(qualquer outro valor encerrará o pedido)\n" ).upper()
            if parar == "S":
                os.system("cls")
            else:
                break
        case _:
            input("Valor inválido. Aperte qualquer coisa parar retornar")
            os.system("cls")

print("Pratos do pedido:")
for i in range(quantidade):
    print(f"-{pratos[i]}/ R${valores[i]}")

print
print(f"Valor total do pedido:R${sum(valores)}")