import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str

@dataclass
class pessoa:
    
    nome: str
    email: str
    endereco: Endereco

    def mostrar_dados(self):
        print("---Dados---")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Endereço:\n -Logradouro: {self.endereco.logradouro}\n -Número: {self.endereco.numero}\n -Cidade: {self.endereco.cidade}")

cliente = pessoa(nome= input("Digite seu nome:\n"),
                  email= input("Digite seu email:\n"),
                    endereco= Endereco(logradouro= input("Digite sua rua:\n"),
                                        numero= input("Digite o número:\n"),
                                          cidade= input("Digite sua cidade:\n")))

cliente.mostrar_dados()
