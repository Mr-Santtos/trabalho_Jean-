matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matriz)
soma_principal = 0
soma_secundaria = 0

for i in range(n):
    soma_principal += matriz[i][i]
    soma_secundaria += matriz[i][n - 1 - i]

print(f"Soma diagonal principal: {soma_principal}")
print(f"Soma diagonal secundária: {soma_secundaria}")
