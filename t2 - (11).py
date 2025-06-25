inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))
soma = 0

for i in range(min(inicio, fim)+1, max(inicio, fim)):
    print(i)
    soma += i

print("Soma dos números do intervalo:", soma)
