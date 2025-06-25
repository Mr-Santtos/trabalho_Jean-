def realizar_operacao_base(num1_str, num2_str, base_origem, operacao, base_destino):
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

    n1 = para_decimal(num1_str, base_origem)
    n2 = para_decimal(num2_str, base_origem)
    if n1 is None or n2 is None:
        return "Erro: número inválido para a base de origem."

    if operacao == '+':
        res = n1 + n2
    elif operacao == '-':
        res = n1 - n2
    elif operacao == '*':
        res = n1 * n2
    elif operacao == '/':
        if n2 == 0:
            return "Erro: divisão por zero."
        res = round(n1 / n2)
    else:
        return "Erro: operação inválida."

    if res < 0:
        return "Erro: resultado negativo não suportado."

    return de_decimal(res, base_destino)
