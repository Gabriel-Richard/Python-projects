from time import sleep
from random import randint
print('''\033[4mSuas opções\033[m:\n
\033[34m
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA \033[m\n''')

pc = randint(0,2)
jogador = int(input('Qual a sua jogada? '))

sleep(1)
print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print ('PO!!!')

print('-=-'*20)

if jogador == 0:
    print('O JOGADOR ESCOLHEU: PEDRA')
elif jogador == 1:
    print('O JOGADOR ESCOLHEU: PAPEL.')
elif jogador == 2:
    print('JOGADOR ESCOLHEU: TESOURA.')

if pc == 0:
    print('O COMPUTADOR ESCOLHEU: PEDRA.')
elif pc == 1:
    print('O COMPUTADOR ESCOLHEU: PAPEL.')
elif pc == 2:
    print('O COMPUTADOR ESCOLHEU: TESOURA.')

if jogador == 0 and pc == 1 or jogador == 1 and pc == 2 or jogador == 2 and pc == 0:
    print('JOGADOR \033[31mPERDEU!\033[m')
elif jogador == 0 and pc == 2 or jogador == 1 and pc == 0 or jogador == 2 and pc == 1:
    print('JOGADOR \033[32mmVITORIA!!!\033[m')
else:
   print('\033[36mEMPATE!\033[m')
print('-=-' * 20)

# poderia ter usado o modo
# itens = (PEDRA, PAPEL, TESOURA)
# print('Computador jogou {}'.format(itens[pc]))
# print('Jogador jogou{}'.format(itens[jogador]))
