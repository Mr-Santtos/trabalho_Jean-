contadores = [0, 0, 0, 0]  

while True:
    num = int(input("Número positivo (negativo para sair): "))
    if num < 0:
        break
    if 0 <= num <= 25:
        contadores[0] += 1
    elif 26 <= num <= 50:
        contadores[1] += 1
    elif 51 <= num <= 75:
        contadores[2] += 1
    elif 76 <= num <= 100:
        contadores[3] += 1

print(f"[0-25]: {contadores[0]}")
print(f"[26-50]: {contadores[1]}")
print(f"[51-75]: {contadores[2]}")
print(f"[76-100]: {contadores[3]}")
