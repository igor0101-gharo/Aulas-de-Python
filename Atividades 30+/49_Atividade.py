import os
os.system("cls")
from dataclasses import dataclass
import time

@dataclass
class pessoa:
    nome: str
    cpf: str
    telefone: str

    def mostrar_dados(self):
        print("---Dados completos---")
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone:{self.telefone}")

    def dados_sms_marketing(self):
        print("---Telefone para marketing---")
        print(f"Telefone:{self.telefone}")
        
lista_de_clientes =[]

for i in range(3):
    cliente = pessoa(nome= input("Digite o seu nome:\n"),
                     cpf= input("Digite o seu CPF:\n"),
                     telefone= input("Digite o seu Telefone:\n"))
    lista_de_clientes.append(cliente)
    os.system("cls")

for cliente in lista_de_clientes:
    cliente.mostrar_dados()
    print("\n")
    cliente.dados_sms_marketing()
    print("\n")
    time.sleep(1.5)