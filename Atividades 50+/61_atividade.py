import os
os.system("cls")
from dataclasses import dataclass
import time

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_dadosC(self):
        print(f"-Nome: {self.nome}\n-E-mail: {self.email}\n-Telefone: {self.telefone}\n-Endereço: {self.endereco}\n\n")

@dataclass
class Produto:
    nome: str
    quantidade: int
    lote: str
    validade: str

    def mostrar_dadosP(self):
        print(f"-Produto: {self.nome}\n-Quantidade: {self.quantidade}\n-Lote: {self.lote}\n-Validade: {self.validade}")

lista_clientes = []
lista_produtos = []

def verificar_lista(lista):
    if not lista:
        print("Não há nenhum item cadastrado.")
        return True
    return False

def adicionar_listaC(lista):
    cliente_add = Cliente(nome= input("Digite o nome do cliente.\n"),
                      email= input("Digite o E-mail do cliente.\n"),
                      telefone= input("Digite o telefone de contato.\n"),
                      endereco=input("Digite o endereço do cliente.\n"))
    lista.append(cliente_add)
    print("Cliente adicionado com sucesso!")

def adicionar_listaP(lista):
    produto_add = Produto(nome= input("Digite o nome do produto.\n"),
                          quantidade=int(input("Digite a quantidade recebida no lote.\n")),
                          lote= input("Digite o número do lote.\n"),
                          validade= input("Digite a data de validade do lote.\n"))

    lista.append(produto_add)
    print("Produto adicionado com sucesso.")

def encontrar(lista, nome_buscar):
    nome_buscar_lower = nome_buscar.lowwer()
    for item in lista:
        if item.nome == nome_buscar_lower:
            return item
    return None

def mostrar_listaC(lista):
    if verificar_lista(lista):
        print("Não há itens cadastrados")
        return
    
    print("---Lista de Clientes---")
    for cliente in lista:
        cliente.mostrar_dadosC()


def mostrar_listaP(lista):
    if verificar_lista(lista):
        print("Não há itens cadastrados")
        return
    
    print("---Lista de Produtos---")
    for produto in lista:
        produto.mostrar_dadosP()

def atualizar_cliente(lista):
    if verificar_lista(lista):
        print("Não há itens cadastrados")
        return

    mostrar_listaC(lista)
    nome_buscar = input("Digite o nome do cliente para atualizar.\n")

    nome_att = encontrar(lista, nome_buscar)

    if nome_att:
        print("--- Dados atuais ---")
        nome_att.mostrar_dadosC()
        print("\nDigite os novos dados ou deixe em branco para manter.")
        novo_nome = input("Nome: ")
        novo_email = input("E-mail: ")
        novo_telefone = input("Telefone:  ")
        novo_endereco = input("Endereço:  ")

        if novo_nome:
            nome_att.nome = novo_nome
        if novo_email:
            nome_att.email = novo_email
        if novo_telefone:
            nome_att.telefone = novo_telefone
        if novo_endereco:
            nome_att.endereco = novo_endereco
        
        print("Dados atualizados com sucesso.")
    else:
        print(f" Cliente '{nome_buscar}' não encontrado")

def atualizar_produto(lista):
    if verificar_lista(lista):
        print("Não há itens cadastrados")
        return
        
    
    mostrar_listaP(lista)
    nome_buscar = input("Digite o nome do produto.\n")
    nome_att = encontrar(lista, nome_buscar)

    if nome_att:
        print("--- Dados atuais---")
        nome_att.mostrar_dadosP()
        print("\nDigite os novos dados ou deixe em branco para manter.")
        novo_nome = input("Nome: ")
        nova_quantidade = input("Quantidade: ")
        novo_lote = input("Lote: ")
        nova_validade = input("Validade: ")

        if novo_nome:
            nome_att.nome = novo_nome
        if nova_quantidade:
            nome_att.quantidade = nova_quantidade
        if novo_lote:
            nome_att.lote = novo_lote
        if nova_validade:
            nome_att.validade = nova_validade
        print("Dados atualizados com sucesso.")
    else:
        print(f"produto '{nome_buscar}' não encontrado.")

def excluirC(lista):
    if verificar_lista(lista):
        print("Não há itens cadastrados")
        return

    mostrar_listaC(lista)
    nome_buscar = input("Digite o nome do cliente que deseja excluir.\n")
    nome_excluir = encontrar(lista, nome_buscar)

    if nome_excluir:
        lista.remove(nome_excluir)
        print("Cliente excluído com sucesso.")
    else:
        print(f" Cliente '{nome_buscar}' não encontrado")
        

def excluirP(lista):
    if verificar_lista(lista):
        print("Não há itens cadastrados")
        return

    mostrar_listaP(lista)
    nome_buscar = input("Digite o nome do cliente que deseja excluir.\n")
    nome_excluir = encontrar(lista, nome_buscar)

    if nome_excluir:
        lista.remove(nome_excluir)
        print("Produto excluído com sucesso.")
    else:
        print(f" Produto '{nome_buscar}' não encontrado")
        

        
            
