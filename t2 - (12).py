num = int(input("Digite um número de 1 a 10 para ver a tabuada: "))
print(f"Tabuada de {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
