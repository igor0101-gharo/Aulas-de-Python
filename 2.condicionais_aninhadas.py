#condicionais anhinhada.

import os
os.system("cls")

idade = 20

#O comando "elif" permite colocar uma segunda condição. A primeira condição tem prioridade, ou seja, o processador só irá ler a condição do "elif"
#se a condição do "if" não for satisfeita.
if idade >= 18:
    print("Maior de idade")
elif idade >= 14:
    print("Adolescente")
else:
    print("Criança")

print("FIM")