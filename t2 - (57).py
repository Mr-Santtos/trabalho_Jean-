matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

tamanho_linhas_iguais = all(len(linha) == len(matriz[0]) for linha in matriz)

quadrada = len(matriz) == len(matriz[0])

print(tamanho_linhas_iguais and quadrada)
