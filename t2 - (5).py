while True:
    a = int(input("População do país A: "))
    b = int(input("População do país B: "))
    taxa_a = float(input("Taxa de crescimento de A (%): "))
    taxa_b = float(input("Taxa de crescimento de B (%): "))

    if a > 0 and b > 0 and taxa_a > 0 and taxa_b > 0:
        anos = 0
        while a <= b:
            a += a * (taxa_a / 100)
            b += b * (taxa_b / 100)
            anos += 1
        print(f"População de A ultrapassa B em {anos} anos.")
    else:
        print("Entradas inválidas. Tente novamente.")
    
    repetir = input("Deseja repetir? (s/n): ").lower()
    if repetir != 's':
        break
