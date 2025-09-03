import os 
os.system("cls")

print("PLACEHOLDER TITTLE\n")

#Refazer com "match"
#olhar o comando 'def" para gerar funções e chama-las

def posicao (escolha):
    match escolha:
        case "abrir a porta":
            print("\nVocê tenta abrir a porta")
            print("a porta está trancada\n")
            escolha = input("Digite o que deseja fazer a seguir:\nabrir a porta\nabrir a janela\nabrir o guarda roupa\n")
            posicao(escolha)

        case "abrir a janela":
            print("\nVocê se desequilibrou e caiu da janela. Você morreu.\n FIM")
        case "abrir o guarda roupa":
            print("\nVocê abriu o guarda roupa e encontrou uma chave antiga dentro dele.\n")
            escolha = input("Digite o que deseja fazer a seguir:\nabrir a porta\nabrir a janela\nabrir o guarda roupa\n")
            posicao2(escolha)
        case _:
            print("Opção inválida")
            escolha = input("Digite o comando novamente\n")
            posicao(escolha)

def posicao2 (escolha):
    match escolha:
        case "abrir a porta":
            print("você abriu a porta e escapou.\nParabéns")
        case "abrir a janela":
            print("\nVocê se desequilibrou e caiu da janela. Você morreu.\n FIM")
        case "abrir o guarda roupa":
            print("\nNão há mais nada dentro do Guarda roupa.\n")
            escolha = input("Digite o que deseja fazer a seguir:\nabrir a porta\nabrir a janela\nabrir o guarda roupa\n")
            posicao2(escolha)
        case _:
            print("Opção inválida")
            escolha = input("Digite o comando novamente")
            posicao2




print("você acorda em um quarto desconhecido")
escolha = input("Digite o que deseja fazer a seguir:\nabrir a porta\nabrir a janela\nabrir o guarda roupa\n")
posicao(escolha)
   
      
            
            
             




