linhas = 3
colunas = 4

matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(i * j)
    matriz.append(linha)

for linha in matriz:
    print(linha)
