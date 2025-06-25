divida = float(input("Valor da dívida: R$ "))

parcelas_juros = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}

print("Valor da Dívida | Juros | Parcelas | Valor da Parcela")
for parcelas, juros in parcelas_juros.items():
    valor_juros = divida * (juros / 100)
    valor_total = divida + valor_juros
    valor_parcela = valor_total / parcelas
    print(f"R$ {valor_total:.2f}       {valor_juros:.2f}     {parcelas}        R$ {valor_parcela:.2f}")
