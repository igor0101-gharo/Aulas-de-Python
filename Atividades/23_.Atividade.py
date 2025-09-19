import os
os.system("cls")
preco = 0
while True:
    os.system("cls")
    print("""
    Código\t Prato\t\t Valor
    1\t Picanha\t R$25,00
    2\t Lasanha\t R$20,00
    3\t Strogonoff\t R$18,00
    4\t Bife Acebolado\t R$15,00
    5\t Pão com ovo\t R$5,00      
    """)




    codigo = int(input("Digite o código do prato desejado\n"))
    continuar = 0

    match codigo:
            case 1:
                print("Prato Escolhido:Picanha\nValor: R$ 25,00")
                preco = preco + 25.00
                continuar = int(input("Quer pedir outro prato?\n1.Sim\n2.Não"))
                if continuar == 2:
                    break
                elif continuar == 1:
                    print("Atualizando pedido...\n")
                else:
                    print("valor inválido, encerrando pedido.")
                    break
            case 2:
                print("Prato Escolhido:Lasanha\nValor: R$20,00")
                preco = preco + 20.00
                continuar = int(input("Quer pedir outro prato?\n1.Sim\n2.Não"))
                if continuar == 2:
                    break
                elif continuar == 1:
                    print("Atualizando pedido...\n")
                else:
                    print("valor inválido, encerrando pedido.")
                    break
            case 3:
                print("Prato Escolhido:Strogonoff\nValor: R$18,00")
                preco = preco + 18.00
                continuar = int(input("Quer pedir outro prato?\n1.Sim\n2.Não"))
                if continuar == 2:
                    break
                elif continuar == 1:
                    print("Atualizando pedido...\n")
                else:
                    print("valor inválido, encerrando pedido.")
                    break
            case 4:
                print("Prato Escolhido:Bife Acebolado\nValor: R$15,00")
                preco = preco + 15.00
                continuar = int(input("Quer pedir outro prato?\n1.Sim\n2.Não"))
                if continuar == 2:
                    break
                elif continuar == 1:
                    print("Atualizando pedido...\n")
                else:
                    print("valor inválido, encerrando pedido.")
                    break
            case 5:
                print("Prato Escolhido:Pão com ovo\nValor: R$5,00")
                preco = preco + 5.00
                continuar = int(input("Quer pedir outro prato?\n1.Sim\n2.Não"))
                if continuar == 2:
                    break
                elif continuar == 1:
                    print("Atualizando pedido...\n")
                else:
                    print("valor inválido, encerrando pedido.")
                    break

            case _:
                print("Código Inválido.\nencerrando pedido.")
                break

print(f"O seu pedido custa: R${preco:.2f}")
