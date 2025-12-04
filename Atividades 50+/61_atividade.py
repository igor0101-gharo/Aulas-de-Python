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
    nome_buscar = input("Digite o nome do produto que deseja excluir.\n")
    nome_excluir = encontrar(lista, nome_buscar)

    if nome_excluir:
        lista.remove(nome_excluir)
        print("Produto excluído com sucesso.")
    else:
        print(f" Produto '{nome_buscar}' não encontrado")

def encontrar_cliente(lista):
    if verificar_lista(lista):
        print("Não há itens cadastrados.")
        return

    nome_buscar = input("Digite o nome do cliente que deseja encontrar.\n")
    nome_mostrar = encontrar(lista, nome_buscar)

    if nome_buscar:
        print("--- Dados do Cliente ---")
        nome_buscar.mostrar_dadosC()
    else:
        print("Cliente não encontrado")

def encontrar_produto(lista):
    if verificar_lista(lista):
        print("Não há itens cadastrados.")
        return

    nome_buscar = input("Digite o nome do produto que deseja encontrar.\n")
    nome_mostrar = encontrar(lista, nome_buscar)

    if nome_mostrar:
        print("--- Dados do Produto ---")
        nome_mostrar.mostrar_dadosP()
    else:
        print("Produto não encontrado")


while True:
    try:
        codigo = int(input("""
--- MENU ----
1- Lista de Clientes
2- Lista de Produtos
3- sair"""))
    except ValueError:
        print("Entrada inválida. Digite um número...")
        time.sleep(2)
        os.system("cls")
        continue
    
    match codigo:
        case 1:
            while True:
                try:
                    funcao = int(input("""
---Lista de clientes---
1- Adicionar um cliente
2- Buscar um cliente
3- Mostrar lista
4- Atualizar um cliente
5- Excluir um cliente
6-voltar"""))
                except ValueError:
                    print("Entrada inválida. Digite um número...")
                    time.sleep(2)
                    os.system("cls")
                    continue

                match funcao:
                    case 1: 
                        adicionar_listaC(lista_clientes)
                        input("")
                        os.system("cls")
                    case 2:
                        encontrar_cliente(lista_clientes)
                        input("")
                        os.system("cls")
                    case 3:
                        mostrar_listaC(lista_clientes)
                        input("")
                        os.system("cls")
                    case 4:
                        atualizar_cliente(lista_clientes)
                        input("")
                        os.system("cls")
                    case 5:
                        excluirC(lista_clientes)
                        input("")
                        os.system("cls")
                    case 6:
                        os.system("cls")
                        break
                    case _:
                        os.system("cls")
                        input("Valor inválido. Digite novamente.")
                        os.system("cls")

        case 2:
            while True:
                try:
                    funcao = int(input("""
---Lista de produtos---
1- Adicionar um produto
2- Buscar um produto
3- Mostrar lista
4- Atualizar um produto
5- Excluir um produto
6-voltar"""))
                except ValueError:
                    print("Entrada inválida. Digite um número...")
                    time.sleep(2)
                    os.system("cls")
                    continue

                match funcao:
                    case 1:
                        adicionar_listaP(lista_produtos)
                        input("")
                        os.system("cls")
                    case 2:
                        encontrar_produto(lista_produtos)
                        input("")
                        os.system("cls")
                    case 3:
                        mostrar_listaP(lista_produtos)
                        input("")
                        os.system("cls")
                    case 4:
                        atualizar_produto(lista_produtos)
                        input("")
                        os.system("cls")
                    case 5:
                        excluirP(lista_produtos)
                        input("")
                        os.system("cls")
                    case 6:
                        os.system("cls")
                        break
                    case _:
                        os.system("cls")
                        input("Valor inválido.digite novamente")
                        os.system("cls")


                        

    

        
      
