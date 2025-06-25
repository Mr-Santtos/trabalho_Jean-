matriz = [
    [1, 2, 3],
    [4, 2, 6],
    [7, 8, 2]
]

elemento = int(input("Digite o elemento para contar: "))
contador = 0

for linha in matriz:
    contador += linha.count(elemento)

print(f"O elemento {elemento} aparece {contador} vezes na matriz.")
