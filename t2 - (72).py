def converter_temperatura(valor, unidade_origem, unidade_destino):
    origem = unidade_origem.upper()
    destino = unidade_destino.upper()

    if origem == destino:
        return valor

    if origem == "C":
        c = valor
    elif origem == "F":
        c = (valor - 32) / 1.8
    elif origem == "K":
        c = valor - 273.15
    else:
        return "Unidade de origem inválida."

    if destino == "C":
        return c
    elif destino == "F":
        return c * 1.8 + 32
    elif destino == "K":
        return c + 273.15
    else:
        return "Unidade de destino inválida."
