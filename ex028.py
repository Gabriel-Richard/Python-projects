from random import randint
from time import sleep
print ('=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=\n'
       'Vou pensar em um numero entre 0 a 5 tente adivinhar!\n'
       '=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
n1 = randint(0, 5)
n2 = int(input('digite o numero que pensei: '))
print ('PROCESSANDO...')
sleep (2)
if n2 == n1:
    print('Voce acertou!!!')
else:
    print('GANHEI! eu tnha pensado no numero {} nao no numero {}'.format(n1, n2))