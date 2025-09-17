import os
os.system("cls")

login = "coxinha123"
senha = "quibe456"

while True:
    uselogin = input("Digite o seu Login:\nLogin:")
    usesenha = input("Digite sua senha:\nSenha:")
    if uselogin == login and usesenha == senha:
        print("Você está logado")
        break
    else:
        print("Inválido.tente de novo")