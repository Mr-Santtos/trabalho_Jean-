def combinar_listas(*listas):
    resultado = []
    for lista in listas:
        resultado.extend(lista)
    return resultado
