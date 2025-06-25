temperaturas = []

while True:
    temp = input("Informe a temperatura (ou 'sair' para encerrar): ")
    if temp.lower() == 'sair':
        break
    try:
        temp_val = float(temp)
        temperaturas.append(temp_val)
    except ValueError:
        print("Valor inválido!")

if temperaturas:
    print(f"Menor temperatura: {min(temperaturas):.2f}")
    print(f"Maior temperatura: {max(temperaturas):.2f}")
    print(f"Média das temperaturas: {sum(temperaturas)/len(temperaturas):.2f}")
else:
    print("Nenhuma temperatura informada.")
