import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Aluno:
    nome:str
    idade: int
    email: str
    telefone: str


quantidade_alunos = 2
lista_alunos = []

print("Solicitando dados do aluno.")
for i in range(quantidade_alunos):
    aluno = Aluno(
        nome= input("Digite o nome: "),
        idade= int(input("Digite a idade:")),
        email=input("Digite o e-mail:"),
        telefone=input("Digite o telefone")
    )
    lista_alunos.append(aluno)
    os.system("cls")

print()
print("Salvando dados.")
arquivo = "dados_alunos.txt"

with open(arquivo,"a") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(f"Nome:{aluno.nome}\nIdade:{aluno.idade}\nE-mail:{aluno.email}\nTelefone:{aluno.telefone}\n\n\n")
    print("salvo")

    