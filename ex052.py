n1 = int(input('Digite um nuemro: '))

cont = 0

for c in range (1 , n1 + 1 ):
    if n1 % c == 0:
        cont += 1
        print('\033[31m {}\033[m'.format(c),end= '')
    else:
        print('\033[36m {}\033[m'.format(c),end= '')

print('\n O numero {} foi divisivel {}'.format(n1, cont))

if cont == 2:
    print(' É por isso que ele É PRIMO')
else:
    print(' É por isso que ele NÃO É PRIMO')