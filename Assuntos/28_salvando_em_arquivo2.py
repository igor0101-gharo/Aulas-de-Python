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

nome_do_arquivo = "Dados_pacientes.txt"

with open(nome_do_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_de_pacientes:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade} anos\n")
        print("Dados salvos com sucesso.")

print("\nExibindo lista de pacientes:")
for paciente in lista_de_pacientes:
    paciente.exibir_dados()
