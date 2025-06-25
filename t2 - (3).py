# a) Nome
while True:
    nome = input("Digite o nome: ")
    if len(nome) > 3:
        break
    print("Nome deve ter mais que 3 caracteres.")

# b) Idade
while True:
    idade = int(input("Digite a idade: "))
    if 0 <= idade <= 150:
        break
    print("Idade deve estar entre 0 e 150.")

# c) Salário
while True:
    salario = float(input("Digite o salário: "))
    if salario > 0:
        break
    print("Salário deve ser maior que zero.")

# d) Sexo
while True:
    sexo = input("Digite o sexo (f/m): ").lower()
    if sexo in ['f', 'm']:
        break
    print("Sexo inválido. Use 'f' ou 'm'.")

# e) Estado civil
while True:
    estado = input("Estado civil (s, c, v, d): ").lower()
    if estado in ['s', 'c', 'v', 'd']:
        break
    print("Estado civil inválido.")
