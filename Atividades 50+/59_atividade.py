import os
os.system("cls")
from dataclasses import dataclass


@dataclass
class Funcionario:
    nome: str
    nascimento: str
    cpf: str
    funcao: str

    def mostrar_dados(self):
        print(f"-Nome: {self.nome}\n-Data de nascimento: {self.nascimento}\n-CPF: {self.cpf}\n-Função: {self.funcao}\n\n")

lista_funcionarios = []


def verificar_lista(lista_funcionarios):
    if not lista_funcionarios:
        print("Não há funcionários cadastrados.")
        return True
    return False

def adicionar(lista_funcionarios):
    nome = input("Digite o nome:\n")
    nascimento = input("Digite a data de nascimento:\n")
    cpf = input("Digite o cpf:\n")
    funcao = input("Digite a função:\n")
    
    novo_funcionario = Funcionario(nome=nome , nascimento= nascimento , cpf= cpf , funcao= funcao)
    lista_funcionarios.append(novo_funcionario)
    print("Funcionário cadastrado com sucesso.")

def mostrar_lista(lista_funcionarios):
    if verificar_lista(lista_funcionarios):
        return
    
    print("--- Lista de Funcionários ---")
    for funcionario in lista_funcionarios:
        funcionario.mostrar_dados()

def buscar_funcionario(lista_funcionarios, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for funcionario in lista_funcionarios:
        if funcionario.nome.lower == nome_buscar_lower:
            return funcionario
        return None

def atualizar_funcionario(lista_funcionarios):
    if verificar_lista(lista_funcionarios):
        return
    
    mostrar_lista(lista_funcionarios)
    nome_buscar = input("\n-Qual funcionário deseja atualizar?\n-Digite o nome.")
    funcionario_atualizar = buscar_funcionario(lista_funcionarios, nome_buscar= nome_buscar)

    if funcionario_atualizar:
        print("Funcionário encontrado")
        print("Digite novos dados ou deixe em branco para manter.")

        print(f"Nome atual: {funcionario_atualizar.nome}")
        novo_nome = input("Digite o novo nome:\n")

        print(f"Data de nascimento atual: {funcionario_atualizar.nascimento}")
        nova_data = input("Digite a nova data:\n")

        print(f"CPF atual: {funcionario_atualizar.cpf}")
        novo_cpf = input("Digite o novo CPF:\n")

        print(f"Função atual: {funcionario_atualizar.funcao}")
        nova_funcao = input("Digite a nova função:\n")

        if novo_nome:
            funcionario_atualizar.nome = novo_nome
        if nova_data:
            funcionario_atualizar.nascimento = nova_data
        if novo_cpf:
            funcionario_atualizar.cpf = novo_cpf
        if nova_funcao:
            funcionario_atualizar.funcao = nova_funcao
        
        print(f"Dados do funcionário {nome_buscar} atualizados com sucess.")
    else:
        print(f"Funcionário não encontrado.")

def excluir_funcionario(lista_funcionarios):
    if verificar_lista(lista_funcionarios):
        return
    
    mostrar_lista(lista_funcionarios)
    nome_buscar = input("\n-Qual funcionário deseja atualizar?\n-Digite o nome.")
    funcionario_remover = buscar_funcionario(lista_funcionarios, nome_buscar= nome_buscar)

    if funcionario_remover:
        lista_funcionarios.remove(funcionario_remover)
        print("Funcionário removido da lista")
    else:
        print("Funciónário não encontrado.")


while True:
    codigo = int(input("O que deseja?\n1-Adicionar funciónário\n2-Buscar um funcionário\n3-Mostrar a lista\n4-Atualizar informações de um funcionário\n5-remover um funcionário da lista\n6-Sair\n"))

    match codigo:
        case 1:
            adicionar(lista_funcionarios)
            input("")
            os.system("cls")
        case 2:
            nome = input("Digite o nome do funcionário")
            buscar_funcionario(lista_funcionarios , nome)
            input("")
            os.system("cls")
        case 3:
            mostrar_lista(lista_funcionarios)
            input("")
            os.system("cls")
        case 4:
            atualizar_funcionario(lista_funcionarios)
            input("")
            os.system("cls")
        case 5:
            excluir_funcionario(lista_funcionarios)
            input("")
            os.system("cls")
        case 6:
            print("Aplicação encerrada.")
            break
        case _:
            input("valor inválido.")
            
            





