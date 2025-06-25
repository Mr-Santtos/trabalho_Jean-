gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

maior = 0
menor = 10
total_alunos = 0
soma_notas = 0

while True:
    usar = input("Outro aluno vai usar o sistema? (s/n): ").lower()
    if usar != 's':
        break

    acertos = 0
    for i in range(10):
        resposta = input(f"Resposta da questão {i+1}: ").upper()
        if resposta == gabarito[i]:
            acertos += 1

    print(f"Acertos: {acertos}")
    total_alunos += 1
    soma_notas += acertos

    if acertos > maior:
        maior = acertos
    if acertos < menor:
        menor = acertos

if total_alunos > 0:
    print(f"Maior acerto: {maior}")
    print(f"Menor acerto: {menor}")
    print(f"Total de alunos: {total_alunos}")
    print(f"Média da turma: {soma_notas / total_alunos:.2f}")
else:
    print("Nenhum aluno participou.")
