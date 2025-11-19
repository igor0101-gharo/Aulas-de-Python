import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome:str
    idade: int
    peso: float
    altura: float
    cpf: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade} anos\nPeso: {self.peso}kg\nAltura: {self.altura}m\nCPF: {self.cpf}\n\n")

lista_de_pessoas = []
quantidade_de_pessoas = int(input("Quantas pessoas deseja acrescentar ao documento?"))

for i in range(quantidade_de_pessoas):
    pessoa = Pessoa(
        nome=input("Digite o nome:\n"),
        idade= int(input("Digite a idade:\n")),
        peso= float(input("Digite o peso(kg):\n")),
        altura=float(input("Digite a altura(m):\n")),
        cpf=input("Digite o cpf:\n")
    )
    lista_de_pessoas.append(pessoa)
    os.system("cls")

nome_do_arquivo = "dados_pessoas.txt"
with open(nome_do_arquivo, "a") as arquivo_pessoas:
    for pessoa in lista_de_pessoas:
        arquivo_pessoas.write(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade} anos\nPeso: {pessoa.peso}kg\nAltura: {pessoa.altura}m\nCPF: {pessoa.cpf}\n\n")
print("Dados salvos com sucesso")

print("Exibindo acrescimos ao documento.")
for pessoa in lista_de_pessoas:
    pessoa.exibir_dados()




