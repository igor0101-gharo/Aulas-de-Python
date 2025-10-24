import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class pessoa:
    nome:str
    idade: int
    peso: float
    altura: float
    
    def mostrar_dados(self):
        print(f"Nome:{self.nome}")
        print(f"Idade:{self.idade}")
        print(f"Peso:{self.peso:.2f}")
        print(f"Altura:{self.altura:.2f}\n")
    


lista_de_pessoas = []
for i in range(4):
    humano = pessoa(nome=input("Digite seu nome:\n"),
                    idade= int(input("Digite sua idade:\n")),
                    peso=float(input("Digite o seu peso:\n")),
                    altura=float(input("Digite a sua altura:\n")))
    lista_de_pessoas.append(humano)
    os.system("cls")

print("---Dados da lista---")

for index, humano in enumerate(lista_de_pessoas):
    print(f"---{index+1}ª Pessoa---")
    humano.mostrar_dados()

