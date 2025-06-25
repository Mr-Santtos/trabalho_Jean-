total_eleitores = int(input("Número total de eleitores: "))

votos = [0, 0, 0]

for i in range(total_eleitores):
    voto = int(input(f"Eleitor {i+1}, vote no candidato (1, 2 ou 3): "))
    while voto not in [1, 2, 3]:
        print("Voto inválido!")
        voto = int(input(f"Eleitor {i+1}, vote no candidato (1, 2 ou 3): "))
    votos[voto-1] += 1

for i, v in enumerate(votos, start=1):
    print(f"Candidato {i} recebeu {v} votos.")
