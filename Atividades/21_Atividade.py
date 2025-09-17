import os
os.system("cls")

login = "coxinha123"
senha = "quibe456"
tentativas = 0

while True:
    if tentativas == 3:
        print("Número de tentativas excedidas")
        break
    uselogin = input("Digite o seu Login:\nLogin:")
    usesenha = input("Digite sua senha:\nSenha:")
    if uselogin == login and usesenha == senha:
        print("Você está logado")
        break
    else:
        print("Inválido.")
        #tentativas = tentativas+1
        tentativas += 1