import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Aluno:
    nome:str
    idade: int

quantidade_alunos = 2
lista_alunos = []

print("Solicitando dados do aluno.")
for i in range(quantidade_alunos):
    aluno = Aluno(
        nome= input("Digite seu nome: "),
        idade= int(input("Digite sua idade:"))
    )
    lista_alunos.append(aluno)

print()
print("Salvando dados.")
arquivo = "dados_alunos.txt"

with open(arquivo,"w") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f"{aluno.nome},{aluno.idade}\n")
    print("salvo")

    