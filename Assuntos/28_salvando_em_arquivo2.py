import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}")
    
lista_de_pacientes = []
quantidade_de_pacientes = 2

for i in range(quantidade_de_pacientes):
    paciente = Paciente(
        nome=input("Digite o seu nome:"),
        idade = int(input("Digite a idade:"))
    )
    lista_de_pacientes.append(paciente)
    print()

nome_do_arquivo = "Dados_pacientes.csv"

with open(nome_do_arquivo, "a", encoding= "uft-8") as arquivo_pacientes:
    for paciente in lista_de_pacientes:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade} anos\n")
        print("Dados salvos com sucesso.")

#print("\nExibindo lista de pacientes:")
#for paciente in lista_de_pacientes:
#    paciente.exibir_dados()

#print("\nExibindo todos os pacientes:")
#try:
#    # r = read
#    with open(nome_do_arquivo, "r") as arquivo:
#        # Recebe todos os dados do arquivo de uma só vez.
#        lista_todos_pacientes = arquivo.readlines()
#        for paciente in lista_todos_pacientes:
#            print(f"- {paciente.strip()}")
#except FileNotFoundError:
#    print("O arquivo não foi encontrado.")

print("\nExibindo todos os pacientes:")
lista=[]
try:
    # r = read
    # enconding = para resolver acentuação
    with open(nome_do_arquivo, "r", encoding="uft-8") as arquivo:
        # Recebe todos os dados do arquivo de uma só vez.
        lista_todos_pacientes = arquivo.readlines()
        for paciente in lista_todos_pacientes:
            nome, idade = paciente.strip().split(",")
            dados_paciente = Paciente(nome=nome, idade=int(idade))
            lista.append(dados_paciente)
        for paciente in lista:
            paciente.exibir_dados()
            
except FileNotFoundError:
    print("O arquivo não foi encontrado.")