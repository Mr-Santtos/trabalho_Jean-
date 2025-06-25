n = int(input("Quantas pessoas na turma? "))
soma = 0

for i in range(n):
    idade = int(input(f"Idade da {i+1}ª pessoa: "))
    soma += idade

media = soma / n

if media <= 25:
    print("Turma jovem")
elif media <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")
