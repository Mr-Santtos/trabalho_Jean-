num_turmas = int(input("Quantidade de turmas: "))

total_alunos = 0
for i in range(num_turmas):
    alunos = int(input(f"Quantidade de alunos na turma {i+1} (máx 40): "))
    while alunos > 40:
        print("Turma não pode ter mais que 40 alunos.")
        alunos = int(input(f"Quantidade de alunos na turma {i+1} (máx 40): "))
    total_alunos += alunos

media = total_alunos / num_turmas if num_turmas > 0 else 0
print(f"Número médio de alunos por turma: {media:.2f}")
