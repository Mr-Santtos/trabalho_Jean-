def converter_base(numero_str, base_origem, base_destino):
    
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
            num //=base
        return resultado

    dec = para_decimal(numero_str, base_origem)
    if dec is None:
        return "Erro: número inválido para a base de origem."
    return de_decimal(dec, base_destino)
