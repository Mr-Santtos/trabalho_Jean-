def somar_em_bases(lista_numeros, base_origem, base_destino):
    digitos = "0123456789ABCDEF"

    def para_decimal(num_str, base):
        num_str = num_str.upper()
        valor = 0
        for char in num_str:
            if char not in digitos[:base]:
                return None
            valor = valor * base + digitos.index(char)
        return valor

    def de_decimal(num, base):
        if num == 0:
            return "0"
        resultado = ""
        while num > 0:
            resultado = digitos[num % base] + resultado
            num //= base
        return resultado

    total = 0
    for num_str in lista_numeros:
        dec = para_decimal(num_str, base_origem)
        if dec is None:
            return f"Erro: '{num_str}' inválido para base {base_origem}."
        total += dec
    return de_decimal(total, base_destino)
