import string

def contar_palavras(lista_de_frases):
    contador = {}
    for frase in lista_de_frases:
        frase = frase.lower()
        for pontuacao in string.punctuation:
            frase = frase.replace(pontuacao, '')
        palavras = frase.split()
        for palavra in palavras:
            contador[palavra] = contador.get(palavra, 0) + 1
    return contador

frases = [
    "Olá, mundo Python!",
    "Python é divertido. Mundo de programação."
]

print(contar_palavras(frases))
