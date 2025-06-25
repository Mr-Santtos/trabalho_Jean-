def sao_anagramas(palavra1, palavra2):
    p1 = ''.join(sorted(palavra1.replace(" ", "").lower()))
    p2 = ''.join(sorted(palavra2.replace(" ", "").lower()))
    return p1 == p2
