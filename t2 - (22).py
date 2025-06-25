n = int(input("Digite um número inteiro: "))
divisores = []

for i in range(2, n):
    if n % i == 0:
        divisores.append(i)

if not divisores:
    print(f"{n} é primo.")
else:
    print(f"{n} não é primo. Divisores: {divisores}")
