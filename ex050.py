acumulador = 0
for c in range (0,6):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        acumulador = acumulador + n1
print(acumulador)