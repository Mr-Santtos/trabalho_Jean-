alunos = []

for _ in range(10):
    numero = int(input("Número do aluno: "))
    altura = float(input("Altura (cm): "))
    alunos.append((numero, altura))

mais_alto = max(alunos, key=lambda x: x[1])
mais_baixo = min(alunos, key=lambda x: x[1])

print(f"Aluno mais alto: Número {mais_alto[0]}, Altura {mais_alto[1]} cm")
print(f"Aluno mais baixo: Número {mais_baixo[0]}, Altura {mais_baixo[1]} cm")
