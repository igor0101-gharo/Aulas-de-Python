import os
from dataclasses import dataclass
os.system("cls || clear") #limpa o terminal em windows e  Linux
import time

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    
    #Método para mostrar as informações dos clientes
    #Método é o nome dado a uma função que pertence à classe
    def mostrar_dados(self):
        print(f"Nome: {self.nome} \nE-mail: {self.email}\nTelefone: {self.telefone}\n")

lista_clientes = []
#Função para verificar se a lista está vazia
def verificar_lista(lista_clientes):
    if not lista_clientes:
        print("\nNão há clientes cadastrados.")
        return True
    return False

def adicionar_cliente(lista_clientes):
    print("\n--- Adicionar novo cliente ---")
    nome = input("Digite o seu nome:\n")
    email = input("Digite o seu e-mail:\n")
    telefone = input("Digite o seu telefone:\n")

    novo_cliente = Cliente(nome=nome, email=email , telefone= telefone)
    lista_clientes.append(novo_cliente)
    print(f"\nCliente {nome} adicionado com sucesso!")

#Função para encontrar um cliente na lista
def encontrar_cliente_email(lista_clientes, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for cliente in lista_clientes:
        if cliente.email.lower() == nome_buscar_lower:
            return cliente
    return None #None significa retornar vazio, sem conteúdo

def mostrar_todos_clientes(lista_clientes):
    if verificar_lista(lista_clientes):
        return
    
    print("\n--- Lista de clientes ---")
    for cliente in lista_clientes:
        cliente.mostrar_dados()

#Função para atualizar clientes
def atualizar_clientes(lista_clientes):
    if verificar_lista(lista_clientes):
        return
    
    #mostrar lista para ajudar o usuário
    mostrar_todos_clientes(lista_clientes)
    print("--- Atualizar dados do cliente ---")
    email_buscar = input("\nDigite o E-mail do cliente:\n")
    cliente_para_atualizar = encontrar_cliente_email(lista_clientes, nome_buscar= email_buscar)
    
    if cliente_para_atualizar:
        print("\nPessoa encontrada.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"Nome atual: {cliente_para_atualizar.nome}")
        novo_nome = input(f"Novo nome:  ")
        
        print(f"E-mail atual: {cliente_para_atualizar.email}")
        novo_email = input(f"Novo E-mail:  ")
        
        print(f"Telefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone = input(f"Novo telefone")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone
        
        print(f"\nDados do E-mail: {email_buscar} atualizados com sucesso!")
    
    else:
        print(f"\nCliente com E-mail: {email_buscar} não encontrado")

#função para excluir cliente
def excluir_cliente(lista_clientes):
    if verificar_lista(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes)

    email_buscar = input("\nDigite o E-mail que você deseja excluir: ")

    cliente_para_remover = encontrar_cliente_email(lista_clientes, email_buscar)

    if cliente_para_remover:
        lista_clientes.remove(cliente_para_remover)
        print(f"E-mail do cliente: {cliente_para_remover.email} excluido com sucesso!")
    else:
        print(f"\nCliente com o E-mail: {email_buscar} não encontrado.")



#Mostrando menu
while True:
    try:
        codigo = int(input("""
---Gerenciador de Clientes---
1 - Adicionar
2 - Mostrar dados
3 - Atualizar
4 - Excluir
0 - Sair\n\n"""))
    except ValueError:
        print("Entrada inválida. Digite um número...")
        time.sleep(2)
        os.system("cls")
        continue
    
    os.system("cls")
    match codigo:
        case 1:
            adicionar_cliente(lista_clientes)
            input("")
            os.system("cls")
        case 2:
            mostrar_todos_clientes(lista_clientes)
            input("")
            os.system("cls")
        case 3: 
            atualizar_clientes(lista_clientes)
            input("")
            os.system("cls")
        case 4:
            excluir_cliente(lista_clientes)
            input("")
            os.system("cls")
        case 0:
            print("Encerrando...")
            break
        case _:
            input("Valor inválido.")
            os.system("cls")





        
