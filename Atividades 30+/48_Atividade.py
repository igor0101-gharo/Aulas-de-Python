import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class contato:
    nome: str
    email: str
    endereco: str

    def dados_entrega(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco}")

    def dados_nome(self):
        print(f"Nome: {self.nome}")

pessoa1 = contato(nome= input("Digite um nome:\n"),
                 email=input("DIgite o um e-mail:\n"),
                 endereco=input("Digite um endereço:\n"))
pessoa2 = contato(nome= input("Digite um nome:\n"),
                 email=input("DIgite o um e-mail:\n"),
                 endereco=input("Digite um endereço:\n"))

while True:
    codigo = int(input("O que deseja?(digite o número da opção correspondente)\n1.Ver dados completos\n2.Ver apenas nome\n3.Sair"))
    match codigo:
        case 1:
            print("--Primeira pessoa--")
            pessoa1.dados_entrega()
            print("--Segunda pessoa--")
            pessoa2.dados_entrega()
            input("\n_")
            os.system("cls")
        case 2:
            print("--Primeira pessoa--")
            pessoa1.dados_nome()
            print("--Segunda pessoa--")
            pessoa2.dados_nome()
            input("\n_")
            os.system("cls")
        case 3:
            print("Encerrando")
            break
        case _:
            input("Opção inválida")
