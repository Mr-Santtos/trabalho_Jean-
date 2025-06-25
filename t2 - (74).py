def calcular_fatorial_iterativo(n):
    if n < 0:
        return "Número negativo não tem fatorial."
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial

def calcular_fatorial_recursivo(n):
    if n < 0:
        return "Número negativo não tem fatorial."
    if n == 0 or n == 1:
        return 1
    return n * calcular_fatorial_recursivo(n - 1)
