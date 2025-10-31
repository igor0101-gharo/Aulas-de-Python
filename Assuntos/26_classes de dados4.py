import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class endereco:
    logradouro:str
    numero:int

@dataclass
class Pessoa:
    nome:str
    idade: int
    endereco: endereco

    def mostrar_dados(self):
        print(f"Seu nome é {self.nome}, você tem {self.idade} anos e mora na rua {self.endereco.logradouro}, número {self.endereco.numero}")
    


pessoa1 = Pessoa(nome= input("Digite seu nome"), idade= int(input("Digite sua idade")), endereco=endereco(logradouro=input("Digite sua rua"), numero=input("Digite o número da rua")))

pessoa1.mostrar_dados()
