import math
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir: {:.2f} '.format(math.hypot(n1,n2)))
# hi = ( n1 ** 2+ n2 ** 2 ) ** (1/2)