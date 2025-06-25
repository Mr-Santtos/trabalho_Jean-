print("Lojas Tabajara")

while True:
    total = 0.0
    produto_num = 1

    while True:
        preco = float(input(f"Produto {produto_num}: R$ "))
        if preco == 0:
            break
        total += preco
        produto_num += 1

    print(f"Total: R$ {total:.2f}")
    dinheiro = float(input("Dinheiro: R$ "))
    troco = dinheiro - total
    print(f"Troco: R$ {troco:.2f}")
    print()
