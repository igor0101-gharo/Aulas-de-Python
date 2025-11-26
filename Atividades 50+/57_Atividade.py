import os 
os.system("cls")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data_de_admissao: str
    matricula: str
    endereco: str

@dataclass
class Cliente:
    nome: str
    data_de_nascimento: str
    endereco: str

def pedir_dados_f():
      for i in range(3):
                funcionario = Funcionario(
                    nome=input(f"Digite o nome do {i+1}º funcionário\n"),
                    data_de_admissao=input("Digite a data de admissão do funcionário\n"),
                    matricula=input("Digite o número de matrícula do funcióonário\n"),
                    endereco=input("Digite o endereço do funcionário\n")
                    )
                lista_funcionarios.append(funcionario)
                os.system("cls")

def salvar_dados_f():
    with open("Lista_funcionários.txt", "a", encoding= "utf8") as arquivo_funcionarios:
                for funcionario in lista_funcionarios:
                    arquivo_funcionarios.write(f"Nome: {funcionario.nome}\nData de admissão: {funcionario.data_de_admissao}\nMatrícula: {funcionario.matricula}\nEndereço: {funcionario.endereco}\n\n")
                print("Dados salvos com sucesso.")
                input("\n___")

def pedir_dados_c():
    for i in range(3):
        pessoa = Cliente(
             nome= input("Digite o nome do cliente\n"),
             data_de_nascimento= input("Digite a data de nascimento\n"),
             endereco= input("Digite o endereço\n")
        )
        lista_clientes.append(pessoa)
        os.system("cls")

def salvar_dados_c():
    with open("Lista_clientes.txt", "a", encoding= "utf8") as arquivo_clientes:
          for cliente in lista_clientes:
               arquivo_clientes.write(f"Nome: {cliente.nome}\nData de nascimento: {cliente.data_de_nascimento}\nEndereço: {cliente.endereco}\n\n")
    
    print("Dados salvos com sucesso.")
    input("\n___")
             
            
lista_funcionarios = []
lista_clientes = []
while True:
    codigo = int(input("Escolha a opção desejada:\n1. Adicionar Funcionários\n2. Adicionar Clientes\n3. Sair\n"))
    match codigo:
        case 1:
            pedir_dados_f()
            salvar_dados_f()
            os.system("cls")
        case 2:
            pedir_dados_c()
            salvar_dados_c()
            os.system("cls")
        case 3:
            print("Encerrando.")
            break
        case _:
            input("Valor inválido.")
            os.system("cls")
