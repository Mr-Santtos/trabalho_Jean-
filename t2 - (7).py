maior = None
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    if maior is None or num > maior:
        maior = num
print("Maior número:", maior)
