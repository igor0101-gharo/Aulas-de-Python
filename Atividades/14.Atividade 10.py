import os
os.system("cls")

print(""""
Código\t Prato\t\t Valor
  1\t Picanha\t R$25,00
  2\t Lasanha\t R$20,00
  3\t Strogonoff\t R$18,00
  4\t Bife Acebolado\t R$15,00
  5\t Pão com ovo\t R$5,00      
""")

estado = True
while estado == True:
 codigo = int(input("Digite o código do prato desejado ou digite '0' para sair\n"))

 match codigo:
    case 1:
        print("Prato Escolhido:Picanha\nValor: R$ 25,00")
    case 2:
        print("Prato Escolhido:Lasanha\nValor: R$20,00")
    case 3:
        print("Prato Escolhido:Strogonoff\nValor: R$18,00")
    case 4:
        print("Prato Escolhido:Bife Acebolado\nValor: R$15,00")
    case 5:
        print("Prato Escolhido:Pão com ovo\nValor: R$5,00")
    case 0:
        print("Aplicação encerrada")
        estado = False
    case _:
        print("Código Inválido")
