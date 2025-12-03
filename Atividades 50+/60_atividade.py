import os
os.system("cls")
from dataclasses import dataclass
import time

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

def buscar_aluno(lista_alunos, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for aluno in lista_alunos:
        if aluno.nome.lower() == nome_buscar_lower:
            return aluno
    return None

def informar_aluno(lista_alunos, nome_buscar):
    aluno = buscar_aluno(lista_alunos, nome_buscar)
    aluno.mostrar_tudo()

def atualizar_aluno(lista_alunos):
    if verificar_lista(lista_alunos):
        return

    mostrar_lista(lista_alunos)

    nome_atualizar_buscar = input ("Qual Aluno você deseja atualizar informações?\n")
    nome_atualizar = buscar_aluno(lista_alunos, nome_atualizar_buscar)

    if nome_atualizar:
        print("Digite as novas informções ou deixe em branco para manter.")
        print(f"Nome atual: {nome_atualizar.nome}\n")
        novo_nome = input("Digite o novo nome:\n")
        os.system("cls")
        print(f"Data de nascimento atual: {nome_atualizar.nascimento}\n")
        novo_nascimento = input("Digite a nova data de nascimento:\n")
        os.system("cls")
        print(f"R.A atual: {nome_atualizar.ra}\n")
        novo_ra = input("Digite o novo R.A:\n")
        os.system("cls")
        print(f"Curso atual: {nome_atualizar.curso}\n")
        novo_curso = input("Digite o novo curso:\n")
        confirmacao = input("Deseja alterar o endereço?(s/n)").lower()
        if confirmacao == "s":
            print("Endereço atual:\n\n")
            nome_atualizar.mostrar_endereco()
            print("")
            novo_rua = input("Digite a nova rua:\n")
            novo_numero = input("Digite o novo número da residência:\n")
            nova_cidade = input("Digite a nova cidade:\n")
            novo_estado = input("Digite o novo estado:\n")

        if novo_nome:
            nome_atualizar.nome = novo_nome
        if novo_nascimento:
            nome_atualizar.nascimento = novo_nascimento
        if novo_ra:
            nome_atualizar.ra = novo_ra
        if novo_curso:
            nome_atualizar.curso = novo_curso
        if confirmacao == "s":
            if novo_rua:
                nome_atualizar.endereco.logradouro = novo_rua
            if novo_numero:
                nome_atualizar.endereco.numero = novo_numero
            if nova_cidade:
                nome_atualizar.endereco.cidade = nova_cidade
            if novo_estado:
                nome_atualizar.endereco.estado = novo_estado
        print("Dados atualizados.")
    else:
        print("Aluno não encontrado.")

def excluir_aluno(lista_alunos):
    if verificar_lista(lista_alunos):
        return

    mostrar_lista(lista_alunos)

    nome_buscar = input("Digite o nome do aluno que deseja excluir:\n")

    nome_excluir = buscar_aluno(lista_alunos, nome_buscar)

    if nome_excluir:
        lista_alunos.remove(nome_excluir)
        print("Aluno excluido com sucesso.")
    else:
        print("Aluno não encontrado.")


while True:
    try:
        codigo = int(input("""
--- Gerenciador de Alunos---
1- Adicionar Aluno.
2- Buscar Aluno
3- Atualizar Aluno
4- Excluir aluno
5- Mostrar lista
6- Sair\n\n"""))
    except ValueError:
        print("Entrada inválida. Digite um número...")
        time.sleep(2)
        os.system("cls")
        continue
    os.system("cls")
    match codigo:
        case 1:
            adicionar_aluno(lista_alunos)
            input("")
            os.system("cls")
        case 2:
            aluno_buscar = input("Digite o nome do aluno:\n")
            informar_aluno(lista_alunos, aluno_buscar)
            input("")
            os.system("cls")
        case 3:
            atualizar_aluno(lista_alunos)
            input("")
            os.system("cls")
        case 4:
            excluir_aluno(lista_alunos)
            input("")
            os.system("cls")
        case 5:
            mostrar_lista(lista_alunos)
            input("")
            os.system("cls")
        case 6:
            print("aplicação encerrada.")
            break
        case _:
            input("Valor inválido.")

        


            

                










