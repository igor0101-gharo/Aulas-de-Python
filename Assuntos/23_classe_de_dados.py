import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    #dois pontos
    nome: str
    idade: int
    cpf: str

@dataclass
class Pet:
    nome:str
    idade: int
    peso: float

pessoa1 = Pessoa("Alice", 30, "655.488.089-75")
pet1 = Pet("totó", 4, 30)

print(f"Nome: {pessoa1.nome}\nIdade:{pessoa1.idade}\nCPF: {pessoa1.cpf}\n")
print(f"Nome: {pet1.nome}\nIdade:{pet1.idade}\nPeso: {pet1.peso}")
