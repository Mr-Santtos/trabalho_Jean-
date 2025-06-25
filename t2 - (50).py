n = int(input("Digite o valor de N: "))

soma = 0.0
for i in range(1, n+1):
    soma += 1 / i

print(f"Soma da série harmônica até 1/{n}: {soma:.4f}")
