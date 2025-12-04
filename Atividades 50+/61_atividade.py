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

def adicionar_lista(lista):