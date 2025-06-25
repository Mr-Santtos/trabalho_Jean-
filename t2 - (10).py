inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

for i in range(min(inicio, fim)+1, max(inicio, fim)):
    print(i)
