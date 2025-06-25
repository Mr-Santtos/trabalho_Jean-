preco_pao = float(input("Preço do pão: R$ "))

print("Panificadora Pão de Ontem - Tabela de preços")
for i in range(1, 51):
    total = preco_pao * i
    print(f"{i} - R$ {total:.2f}")
