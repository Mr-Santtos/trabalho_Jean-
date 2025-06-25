n = int(input("Digite um número inteiro: "))
primo = True

if n < 2:
    primo = False
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            primo = False
            break

if primo:
    print(f"{n} é primo.")
else:
    print(f"{n} não é primo.")
