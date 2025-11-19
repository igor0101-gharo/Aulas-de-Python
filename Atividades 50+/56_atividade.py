import os
os.system("cls")
from dataclasses import dataclass

lista_funcionarios = []

@dataclass
class Pessoa:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str

def arquivar(lista):
    with open("Funcionarios.csv", "a") as arquivo_funcionarios:
        for funcionario in lista:
            arquivo_funcionarios.write(f"Nome: {funcionario.nome}\nData de nascimento: {funcionario.data_nascimento}\nRG: {funcionario.rg}\nCPF: {funcionario.cpf}\n\n")
        input("arquivos salvos")


def mostrar_dados():
    try:
         with open("Funcionarios.csv", "r") as arquivo_funcionarios:
            todos_funcionarios = arquivo_funcionarios.readlines()
            for funcionario in todos_funcionarios:
                print(f"-{funcionario.strip()}")
    except FileNotFoundError:
        print("Arquivo não encontrado")

for i in range(5):
    pessoa = Pessoa(
        nome=input("Digite o nome:\n"),
        data_nascimento=input("Digite a data de nascimento:\n"),
        rg=input("Digite o Rg:\n"),
        cpf=input("Digite o CPF:\n")
    )
    lista_funcionarios.append(pessoa)
    os.system("cls")

arquivar(lista_funcionarios)

mostrar_dados()




