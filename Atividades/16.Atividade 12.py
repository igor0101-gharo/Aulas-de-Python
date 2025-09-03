import os
os.system("cls")

valor = float(input("Digite o valor de sua compra:"))
pagamento = input("Digite se o seu pagamento será:\n'1.a vista'\n'2.a prazo':")
print("\n")

match pagamento:
    case "a vista":
        print(f"Valor do produto: {valor}\nForma de pagamento: à vista\nValor do desconto: R${valor*0.1:.2f}\nTotal a Pagar: R${valor*0.9:.2f}")

    case "a prazo":
        parcelas = int (input("Digite o número de parcelas."))
        if parcelas > 6:
            print("Valor não suportado.")
        else:
            print(f"Valor do produto: {valor:.2f}\nForma de pagamento: à prazo\n Quantidade de parcelas:{parcelas}\nValor da parcela: {valor/parcelas:.2f}\n Total a prazo: {valor:.2f}")
    
    case "1":
        print(f"Valor do produto: {valor}\nForma de pagamento: à vista\nValor do desconto: R${valor*0.1:.2f}\nTotal a Pagar: R${valor*0.9:.2f}")

    case "2":
        parcelas = int (input("Digite o número de parcelas."))
        if parcelas > 6:
            print("Valor não suportado.")
        else:
            print(f"Valor do produto: {valor:.2f}\nForma de pagamento: à prazo\n Quantidade de parcelas:{parcelas}\nValor da parcela: {valor/parcelas:.2f}\n Total a prazo: {valor:.2f}")
    case _:
        print("Valor inválido.")
    
