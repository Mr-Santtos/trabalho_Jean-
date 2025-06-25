n = int(input("Quantos números deseja digitar? "))
soma = 0
menor = maior = None

for i in range(n):
    while True:
        num = float(input(f"Digite o {i+1}º número (entre 0 e 1000): "))
        if 0 <= num <= 1000:
            break
        print("Número inválido.")
    soma += num
    if menor is None or num < menor:
        menor = num
    if maior is None or num > maior:
        maior = num

print("Menor:", menor)
print("Maior:", maior)
print("Soma:", soma)
