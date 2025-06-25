n = int(input("Quantos termos da série de Fibonacci você quer? "))
a, b = 1, 1
print(a, b, end=' ')
for i in range(n-2):
    a, b = b, a + b
    print(b, end=' ')
print()
