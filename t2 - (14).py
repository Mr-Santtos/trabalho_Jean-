pares = 0
impares = 0

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares:", pares)
print("Ímpares:", impares)
