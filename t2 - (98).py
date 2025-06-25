def encontrar_palindromos_base(lista_numeros_decimais, base):
    digitos = "0123456789ABCDEF"

    def de_decimal(num, base):
        if num == 0:
            return "0"
        resultado = ""
        while num > 0:
            resultado = digitos[num % base] + resultado
            num //= base
        return resultado

    palindromos = []
    for num in lista_numeros_decimais:
        rep = de_decimal(num, base)
        if rep == rep[::-1]:
            palindromos.append(num)
    return palindromos
