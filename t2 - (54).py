matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

transposta = []

for j in range(len(matriz[0])):
    linha_transposta = []
    for i in range(len(matriz)):
        linha_transposta.append(matriz[i][j])
    transposta.append(linha_transposta)

print("Matriz original:")
for linha in matriz:
    print(linha)

print("Matriz transposta:")
for linha in transposta:
    print(linha)
