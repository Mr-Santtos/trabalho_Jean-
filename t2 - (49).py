n = int(input("Número de termos: "))

soma = 0
for i in range(1, n+1):
    soma += i / (2*i - 1)
    print(f"{i}/{2*i - 1}")

print(f"Soma da série: {soma:.4f}")
