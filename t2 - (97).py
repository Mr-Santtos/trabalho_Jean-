def validar_numeros_base(lista_de_strings, base):
    digitos = "0123456789ABCDEF"
    validos = []

    for num_str in lista_de_strings:
        num_str = num_str.strip().upper()
        if not num_str:
            continue
        if all(char in digitos[:base] for char in num_str):
            validos.append(num_str)
    return validos
