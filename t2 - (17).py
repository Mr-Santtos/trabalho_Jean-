n = int(input("Digite um número inteiro para calcular o fatorial: "))
fatorial = 1

for i in range(n, 0, -1):
    fatorial *= i

print(f"{n}! = {fatorial}")
