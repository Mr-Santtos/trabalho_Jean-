n = int(input("Quantas notas deseja inserir? "))
soma = 0

for i in range(n):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += nota

media = soma / n
print("Média das notas:", media)
