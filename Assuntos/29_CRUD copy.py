import os
os.system("cls || clear ")

# CRUD usando lista
# Create = criar / salvar
# Read = buscar / selecionar
# Update = atualizar / modificar
# Delete = excluir

#criando uma lista.
lista_clientes = []
def adicionar():
    nome = input("Digite o nome para adicionar")
    lista_clientes.append(nome)
    print(f"O nome: {nome} foi inserido com sucesso!")
    input("_")
    os.system("cls")


# READ
def Ler():
    print(lista_clientes)
    input("_")
    os.system("cls")

# UPDATE
def update():
    nome_para_atualizar = input("Digite o nome para atualizar")
    if nome_para_atualizar in lista_clientes:
        novo_nome = input("Digite o novo nome")
        indice = lista_clientes.index(nome_para_atualizar)
        lista_clientes[indice] = novo_nome
        print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}.")
    else:
        print(f"O nome {nome_para_atualizar} não foi encontrado.")
    input("_")
    os.system("cls")


# Delete

def delete():
    nome_para_excluir = input("Digite o nome para excluir")
    if nome_para_excluir in lista_clientes:
        lista_clientes.remove(nome_para_excluir)
        print(f"{nome_para_excluir} foi excluido com sucesso!")
    else:
        print(f"O nome {nome_para_excluir} não foi encontrado.")
    input("_")
    os.system("cls")


while True:
    codigo = int(input("Digite o que deseja fazer com a lista:\n1.Ler\n2.Adicionar um nome\n3.Atualizar um nome\n4.Deletar um nome\n5.encerrar aplicação\n"))
    match codigo:
        case 1:
            Ler()
        case 2:
            adicionar()
        case 3:
            update()
        case 4:
            delete()
        case 5:
            os.system("cls")
            print("Aplicação encerrada.")
            break
        case _:
            input("Valor inválido")