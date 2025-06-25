cidades = []

for i in range(5):
    codigo = int(input(f"Código da cidade {i+1}: "))
    veiculos = int(input("Número de veículos de passeio: "))
    acidentes = int(input("Número de acidentes com vítimas: "))
    cidades.append({'codigo': codigo, 'veiculos': veiculos, 'acidentes': acidentes})

maior_indice = max(cidades, key=lambda c: c['acidentes']/c['veiculos'] if c['veiculos'] > 0 else 0)
menor_indice = min(cidades, key=lambda c: c['acidentes']/c['veiculos'] if c['veiculos'] > 0 else 0)
media_veiculos = sum(c['veiculos'] for c in cidades) / 5
cidades_menos_2000 = [c for c in cidades if c['veiculos'] < 2000]
media_acidentes_menos_2000 = (sum(c['acidentes'] for c in cidades_menos_2000) / len(cidades_menos_2000)) if cidades_menos_2000 else 0

print(f"Maior índice de acidentes: Cidade {maior_indice['codigo']}")
print(f"Menor índice de acidentes: Cidade {menor_indice['codigo']}")
print(f"Média de veículos: {media_veiculos:.2f}")
print(f"Média de acidentes em cidades com menos de 2000 veículos: {media_acidentes_menos_2000:.2f}")
