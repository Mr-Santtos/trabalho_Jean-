while True:
    n = int(input("Digite um número para calcular o fatorial (0 a 15): "))
    if 0 <= n <= 15:
        fatorial = 1
        for i in range(1, n+1):
            fatorial *= i
        print(f"{n}! = {fatorial}")
    else:
        print("Número inválido.")
    
    continuar = input("Deseja calcular outro fatorial? (s/n): ")
    if continuar.lower() != 's':
        break
