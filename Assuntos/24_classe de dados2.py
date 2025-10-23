import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome:str
    idade:int
    peso: float
    altura: float

pessoa1 = Pessoa("Igor", 24 , 85.2, 1.8)
#solicitando dados
pessoa2 = Pessoa(nome= input("Digite seu nome"),
                 peso= float(input("Digite seu peso")), 
                 idade= int(input("Digite sua idade")),
                 altura= float(input("Digite sua altura")))

print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade} anos\nPeso: {pessoa1.peso} kg\nAltura: {pessoa1.altura} m\n")
print(f"Nome: {pessoa2.nome}\nIdade: {pessoa2.idade} anos\nPeso: {pessoa2.peso} kg\nAltura: {pessoa2.altura} m")
