limite = int(input("Número inteiro: "))

primos = []
for num in range(2, limite+1):
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        primos.append(num)

print(f"Números primos entre 1 e {limite}:")
print(primos)
