#coding: utf-8

import csv

print("Lendo o documento...")
with open("data/chicago.csv","r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

print("Número de linhas:")
print(len(data_list))

input("Aperte Enter para continuar")

# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.

print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

for line in range(1,21):
    print(line)
    print(data_list[line])


input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas


print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for line in range(1,21):
    print(data_list[line][7])

#tarefa 3