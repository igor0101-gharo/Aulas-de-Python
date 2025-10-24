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

@dataclass 
class teste:
    logradouro: str
    numero: str
    cidade:str

n2 = teste(logradouro="11212121", numero="887878787", cidade= "777879988541")
n1 = Endereco(logradouro= "kkkkkkkk", numero= "5151561", cidade="sdjfndsjfnsd")
cliente = pessoa(nome="igor", email="asmfksafsaf", endereco= n2)
cliente2 = pessoa(nome="igor", email="asmfksafsaf", endereco= n1)

print(f"{cliente.endereco.logradouro}")
print(f"{cliente.endereco.numero}")
print(f"{cliente.endereco.cidade}")
print(f"\n")
print(f"{cliente2.endereco.cidade}")
print(f"{cliente2.endereco.numero}")
print(f"{cliente2.endereco.logradouro}")



