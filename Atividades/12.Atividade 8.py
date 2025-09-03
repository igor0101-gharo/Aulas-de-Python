import os
os.system("cls")

num1= float (input("Digite um número: "))
num2= float (input("Digite outro número: "))

calculo = input("Digite o operador para fazer o cálculo: \n")

match calculo:
    case "+":
        print(f"Números: {num1} e {num2}\nOperador:{calculo}\n Resultado: {num1 + num2}")
    case "-":
        print(f"Números: {num1} e {num2}\nOperador:{calculo}\n Resultado: {num1 - num2}")
    case "*":
        print(f"Números: {num1} e {num2}\nOperador:{calculo}\n Resultado: {num1 * num2}")
    case "/":
        print(f"Números: {num1} e {num2}\nOperador:{calculo}\n Resultado: {num1/num2}")
    case _:
        print("operador inválido")

        