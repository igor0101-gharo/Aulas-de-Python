import os
os.system("cls")

#texto que desejo salvar

texto = input("Digite")

#Definir nome do arquivo para salvar

nome_arquivo = "exemplo.txt"

#comados para salvar - "w" - write(apaga e troca), "a" - append(adiciona sem apagar)
with open(nome_arquivo,"a") as meu_arquivo:
    meu_arquivo.write(f"{texto}\n")
    print("Salvo com sucesso!")