ano_contratacao = 1995
salario = float(input("Salário inicial do funcionário: R$ "))

ano_atual = 2025
percentual = 1.5

for ano in range(ano_contratacao + 1, ano_atual + 1):
    salario += salario * (percentual / 100)
    percentual *= 2

print(f"Salário atual em {ano_atual}: R$ {salario:.2f}")
