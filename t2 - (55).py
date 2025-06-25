matriz = [
    [1, 20, 3],
    [4, 5, 60],
    [7, 8, 9]
]

maior = matriz[0][0]
menor = matriz[0][0]

for linha in matriz:
    for elemento in linha:
        if elemento > maior:
            maior = elemento
        if elemento < menor:
            menor = elemento

print(f"Maior elemento: {maior}")
print(f"Menor elemento: {menor}")
