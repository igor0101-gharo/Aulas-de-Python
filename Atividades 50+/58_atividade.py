import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data_de_admissao: str
    matricula: str
    endereco: str

    def exibir_dadosF(self):
        print(f"-Nome: {self.nome}\n-Data de admissão: {self.data_de_admissao}\n-Matrícula: {self.matricula}\n-Endereço: {self.endereco}\n\n")

@dataclass
class Cliente:
    nome: str
    data_de_nascimento: str
    endereco: str
    
    def exibir_dadosC(self):
        print(f"-Nome: {self.nome}\n-Data de nascimento: {self.data_de_nascimento}\n-Endereço: {self.endereco}\n\n")

lista = []
listaf = []


def adquirir_dados_cliente():
    with open("Lista_clientes.csv", "r", encoding= "utf8") as arquivo:
        lista_todos_clientes = arquivo.readlines()
        for cliente in lista_todos_clientes:
            nome, datanascimento, endereco = cliente.strip().split(",")
            dados_cliente = Cliente(nome= nome , data_de_nascimento= datanascimento , endereco= endereco)
            lista.append(dados_cliente)
        print("--Lista de Clientes--")
        for cliente in lista:
            cliente.exibir_dadosC()

def adquirir_dados_funcionarios():
    with open("Lista_funcionários.csv", "r", encoding= "utf8") as arquivo:
        lista_todos_funcionarios = arquivo.readlines()
        for funcionario in lista_todos_funcionarios:
            nome, data_admissao, matricula, endereco = funcionario.strip().split(",")
            dados_funcionario = Funcionario(nome= nome, data_de_admissao= data_admissao, matricula= matricula, endereco=endereco)
            listaf.append(dados_funcionario)
        print("--Lista de Funcionários--")
        for funcionario in listaf:
            funcionario.exibir_dadosF()

            
            
adquirir_dados_cliente()
adquirir_dados_funcionarios()