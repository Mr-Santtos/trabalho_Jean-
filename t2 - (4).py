a = 80000
b = 200000
anos = 0

while a <= b:
    a *= 1.03
    b *= 1.015
    anos += 1

print(f"Serão necessários {anos} anos para a população de A ultrapassar B.")
