qtd_cds = int(input("Quantidade de CDs: "))

total_valor = 0
for i in range(qtd_cds):
    valor = float(input(f"Valor do CD {i+1}: R$ "))
    total_valor += valor

media = total_valor / qtd_cds if qtd_cds > 0 else 0
print(f"Valor total investido: R$ {total_valor:.2f}")
print(f"Valor médio por CD: R$ {media:.2f}")
