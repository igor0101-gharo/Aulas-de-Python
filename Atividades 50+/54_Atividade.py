import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

    def mostrar_dados(self):
        print(f"Titulo: {self.nome}")
        print(f"Autor : {self.autor}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço: R${self.preco:.2f}\n")

lista_livro = []
for i in range(3):
    livro = Livro(nome=input("Digite o nome do livro:"), autor=input("Digite o autor do livro"), categoria=input("Digite a categoria do livro"), preco= float(input("Digite o preço do livro")))
    lista_livro.append(livro)
    os.system("cls")

arquivo = "catalogo_livros.txt"

with open(arquivo, "a") as arquivo_livros:
    for livro in lista_livro:
        arquivo_livros.write(f"Titulo:{livro.nome}\nAutor:{livro.autor}\nCategoria:{livro.categoria}\nPreço: R${livro.preco}\n\n")
    print("Salvo")
    

