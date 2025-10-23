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
        print(f"Endereço: {self.endereco}")
    
    def dados_email_marketing(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")

pessoa = contato(nome= input("Digite seu nome:\n"),
                 email=input("DIgite o seu e-mail:\n"),
                 endereco=input("Digite seu endereço:\n"))

while True:
    codigo = int(input("O que deseja?(digite o número da opção correspondente)\n1.Ver dados de entrega\n2.Ver dados de marketing\n3.Sair"))
    match codigo:
        case 1:
            pessoa.dados_entrega()
            input("\n_")
            os.system("cls")
        case 2:
            pessoa.dados_email_marketing()
            input("\n_")
            os.system("cls")
        case 3:
            print("Encerrando")
            break
        case _:
            input("Opção inválida")

