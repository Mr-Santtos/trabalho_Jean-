n = int(input("Fatorial de: "))

fatorial = 1
fatores = []
for i in range(n, 0, -1):
    fatorial *= i
    fatores.append(str(i))

expressao = " . ".join(fatores)
print(f"{n}! = {expressao} = {fatorial}")
