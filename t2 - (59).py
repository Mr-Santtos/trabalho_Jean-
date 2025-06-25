texto = input("Digite um texto: ").lower()
vogais = "aeiou"
cont_vogais = 0
cont_consoantes = 0

for letra in texto:
    if letra.isalpha():
        if letra in vogais:
            cont_vogais += 1
        else:
            cont_consoantes += 1

print(f"Vogais: {cont_vogais}")
print(f"Consoantes: {cont_consoantes}")
