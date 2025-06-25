while True:
    nome = input("Atleta: ")
    if nome == "":
        break

    saltos = []
    for i in range(1, 6):
        distancia = float(input(f"{i}º salto: "))
        saltos.append(distancia)

    melhor = max(saltos)
    pior = min(saltos)
    soma = sum(saltos) - melhor - pior
    media = soma / 3

    print(f"Melhor salto: {melhor:.2f} m")
    print(f"Pior salto: {pior:.2f} m")
    print(f"Média dos demais saltos: {media:.2f} m")
    print(f"Resultado final: {nome}: {media:.2f} m\n")
