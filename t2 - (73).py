def filtrar_numeros(lista, tipo):
    tipo = tipo.lower()
    if tipo == 'pares':
        return [x for x in lista if x % 2 == 0]
    elif tipo == 'impares':
        return [x for x in lista if x % 2 != 0]
    elif tipo == 'positivos':
        return [x for x in lista if x > 0]
    elif tipo == 'negativos':
        return [x for x in lista if x < 0]
    else:
        return []
