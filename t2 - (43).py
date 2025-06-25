cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00)
}

total = 0

while True:
    codigo = int(input("Código do item (0 para encerrar): "))
    if codigo == 0:
        break
    if codigo not in cardapio:
        print("Código inválido.")
        continue
    quantidade = int(input("Quantidade: "))
    nome, preco = cardapio[codigo]
    valor = preco * quantidade
    total += valor
    print(f"{nome}: R$ {valor:.2f}")

print(f"Total a pagar: R$ {total:.2f}")
