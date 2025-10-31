#Código para criar uma lista de livros
#dois livros já estão pré-incluidos como exemplo

import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Autor:
    nome:str
    biografia:str

@dataclass
class livro:
    titulo: str
    ano: int
    autor: Autor

    def exibir_detalhes(self):
        print(f"----{self.titulo}----")
        print(f"Ano de publicação: {self.ano}")
        print(f"Autor: {self.autor.nome}")
    
    def exibir_titulos(self):
        print(f"- {self.titulo}")
        

lista_livros = []
exemplo = livro(titulo="Mémorias Póstumas de Brás Cubas", ano=1881, autor=Autor(nome="Machado de Assis", biografia="Nascido no rio" ))
lista_livros.append(exemplo)
exemplo2 = livro(titulo="Meu Pé de Laranja Lima", ano=1968, autor=Autor(nome="José Mauro de Vasconcelos", biografia="Nascido no Brasil" ))
lista_livros.append(exemplo2)

while True:
    opcao = int(input("Digite o que deseja:\n1.Adicionar um livro à lista\n2.procurar um livro na lista\n3.Verificar quantos livros estão cadastrados\n4.Exibir títulos disponíveis\n5.Sair "))
    match opcao:
        case 1:
            os.system("cls")
            adicao = livro(titulo= input("Digite o nome do livro:\n"), ano=int(input("Digite o ano de publicação")), autor=Autor(nome=input("Digite o nome do autor"), biografia=input("Digite a biografia")))
            lista_livros.append(adicao)
            os.system("cls")
        case 2:
            os.system("cls")
            codigo = input("Digite o nome do livro:\n")
            contador = 0

            for livros in lista_livros:
                if livros.titulo == codigo:
                        livros.exibir_detalhes()
                        contador += 1
            if contador == 0:
                print("Não há nenhum livro com esse nome, verifique se você digitou corretamente.")

            
            input("\n_")
            os.system("cls")

        case 5:
            os.system("cls")
            print("encerrando")
            break
        case 3:
            os.system("cls")
            quantidade = len(lista_livros)
            print(f"Atualmente, {quantidade} livro(s) estão cadastrados")
            input("\n_")
            os.system("cls")
        case 4:
            os.system("cls")
            print("---livros disponíveis---")
            for livros in lista_livros:
                livros.exibir_titulos()
            
            input("\n_")
            os.system("cls")

        case _:
            os.system("cls")
            input("Valor inválido")
            os.system("cls")
            

        
              
              
                




