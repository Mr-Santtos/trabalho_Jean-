num = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))

if fim < inicio:
    print("Valor final não pode ser menor que o inicial.")
else:
    print(f"Vou montar a tabuada de {num} começando em {inicio} e terminando em {fim}:")
    for i in range(inicio, fim+1):
        print(f"{num} X {i} = {num*i}")
