candidatos = {1: "José", 2: "João", 3: "Maria", 4: "Ana"}
votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

while True:
    voto = int(input("Digite o voto (0 para encerrar): "))
    if voto == 0:
        break
    if voto in votos:
        votos[voto] += 1
    else:
        print("Voto inválido.")

total_votos = sum(votos.values())

for i in range(1, 5):
    print(f"Votos para {candidatos[i]}: {votos[i]}")
print(f"Votos nulos: {votos[5]}")
print(f"Votos em branco: {votos[6]}")

if total_votos > 0:
    print(f"% votos nulos: {(votos[5]/total_votos)*100:.2f}%")
    print(f"% votos em branco: {(votos[6]/total_votos)*100:.2f}%")
else:
    print("Nenhum voto computado.")
