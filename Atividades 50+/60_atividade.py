import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str
    estado: str

    

@dataclass
class Aluno:
    nome: str
    nascimento: str
    ra: str
    curso: str
    endereco: Endereco

    def mostrar_nome(self):
        print(f"-Nome: {self.nome}\n")

    def mostrar_aluno(self):
        print(f"-Nome: {self.nome}\n-Data de Nascimento: {self.nascimento}\n-R.A: {self.ra}\n-Curso: {self.curso}\n\n")

    def mostrar_endereco(self):
        print(f"O aluno {self.nome} mora na rua {self.endereco.logradouro}, nº {self.endereco.numero},cidade de {self.endereco.cidade}, {self.endereco.estado}")

    def mostrar_tudo(self):
        print(f"-Nome: {self.nome}\n-Data de Nascimento: {self.nascimento}\n-R.A: {self.ra}\n-Curso: {self.curso}\n\n")
        self.mostrar_endereco()

lista_alunos = []

def verificar_lista(lista_alunos):
    if not lista_alunos:
        print("Não há alunos cadastrados.")
        return True
    return False

def adicionar_aluno(lista_alunos):
    nome = input("Digite o nome do aluno:\n")
    os.system("cls")
    nascimento = input("Digite a data de nascimento do aluno:\n")
    os.system("cls")
    numero = input("Digite o R.A do aluno:\n")
    os.system("cls")
    curso = input("Digite o curso em que o aluno está matriculado:\n")
    os.system("cls")
    logradouro = input("Digite o nome da rua em que o aluno mora:\n")
    os.system("cls")
    numero = input("Digite o número da rua:\n")
    os.system("cls")
    cidade = input("Digite a cidade:\n")
    os.system("cls")
    estado = input("Digite o estado:\n")

    endereco_adicionar = Endereco(logradouro= logradouro, 
                                  numero= numero,
                                  cidade=cidade,
                                  estado=estado)
    
    Aluno_adicionar = Aluno(nome=nome ,
                            nascimento= nascimento ,
                            ra=numero,
                            curso= curso,
                            endereco= endereco_adicionar)
    
    lista_alunos.append(Aluno_adicionar)
    print("Aluno adicionado com sucesso.")

def mostrar_lista(lista_alunos):
    if verificar_lista(lista_alunos):
        return
    
    print("--- Lista de Alunos --- ")
    for aluno in lista_alunos:
        aluno.mostrar_nome()





