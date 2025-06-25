codigos = []
alturas = []
pesos = []

while True:
    codigo = int(input("Código do cliente (0 para sair): "))
    if codigo == 0:
        break
    altura = float(input("Altura (m): "))
    peso = float(input("Peso (kg): "))
    codigos.append(codigo)
    alturas.append(altura)
    pesos.append(peso)

if codigos:
    idx_alto = alturas.index(max(alturas))
    idx_baixo = alturas.index(min(alturas))
    idx_gordo = pesos.index(max(pesos))
    idx_magro = pesos.index(min(pesos))

    print(f"Mais alto: código {codigos[idx_alto]}, altura {alturas[idx_alto]:.2f}m")
    print(f"Mais baixo: código {codigos[idx_baixo]}, altura {alturas[idx_baixo]:.2f}m")
    print(f"Mais gordo: código {codigos[idx_gordo]}, peso {pesos[idx_gordo]:.2f}kg")
    print(f"Mais magro: código {codigos[idx_magro]}, peso {pesos[idx_magro]:.2f}kg")
    print(f"Média de alturas: {sum(alturas)/len(alturas):.2f}m")
    print(f"Média de pesos: {sum(pesos)/len(pesos):.2f}kg")
else:
    print("Nenhum dado informado.")
