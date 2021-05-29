from math import factorial
n1 = int(input('Digite um numero para calcular seu fatoral: '))
n2 = n1
n3 = factorial(n1)
print(f'calculando: {n1}! = {n1} x ', end='')
while n2 != 2:
    n2 += - 1
    print( n2, end=' x ')

print( '1 =', n3 )

