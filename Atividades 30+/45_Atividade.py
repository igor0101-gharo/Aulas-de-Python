import os
os.system("cls")

def imc(peso , altura):
    return peso/(altura*altura)

def resultado(imc):
    if imc < 18.5:
        print(f"Seu imc é de {imc:.2f}, você está abaixo do peso ideal.")
        print("Recomendação: Consulte um nutricionista para orientação.")
    elif imc <= 24.9:
        print(f"Seu imc é de {imc:.2f}, Seu peso é normal")
        print("Recomendação: Matenha hábitos saudáveis!")
    elif imc <= 29.9:
        print(f"Seu imc é de {imc:.2f}, você está com sobrepeso.")
        print("Recomendação: Considere uma dieta balanceada e atividade física.")
    elif imc <= 34.9:
        print(f"Seu imc é de {imc:.2f}, você está com obesidade de grau 1.")
        print("Recomendação: Procure orientação de um profissional de saúde.")
    elif imc <= 39.9:
        print(f"Seu imc é de {imc:.2f}, você está com obesidade de grau 2.")
        print("Recomendação: Consulte um médico para avaliação e orientação")
    elif imc >= 40:
        print(f"Seu imc é de {imc:.2f}, você está com obesidade de grau 3.")
        print("Recomendação: Busque assistência médica imediatamente. ")

peso = float(input("Digite seu peso(em kilos):\n"))
altura = float(input("Digite sua altura(em metros):\n"))

resultado_imc = imc(peso, altura)
resultado(resultado_imc)
