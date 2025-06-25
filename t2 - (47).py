while True:
    nome = input("Atleta: ")
    if nome == "":
        break

    notas = []
    for i in range(7):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)

    melhor = max(notas)
    pior = min(notas)
    soma = sum(notas) - melhor - pior
    media = soma / 5

    print(f"Melhor nota: {melhor:.2f}")
    print(f"Pior nota: {pior:.2f}")
    print(f"Média: {media:.2f}\n")
