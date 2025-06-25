def desenhar_triangulo(altura, tipo):
    if tipo == 'esquerda':
        for i in range(1, altura + 1):
            print('*' * i)
    elif tipo == 'direita':
        for i in range(1, altura + 1):
            print(' ' * (altura - i) + '*' * i)
    elif tipo == 'centralizado':
        for i in range(1, altura + 1):
            print(' ' * (altura - i) + '*' * (2 * i - 1))
