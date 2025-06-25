n = int(input("Digite o número de termos (n): "))

soma = 0
for i in range(1, n + 1):
    termo = i / (2 * i - 1)
    print(f"Termo {i}: {termo:.4f}")
    soma += termo

print(f"Soma da série: {soma:.4f}")
