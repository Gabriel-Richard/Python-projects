from random import randint
from time import sleep

print('Oi! sou seu Computador...\n')
sleep(2)
print ('''Acabei de pensar em um numero entre 0 e 10.
Sera que voce consegue adivinhar qual foi?\n''')

rand = randint (0, 10)
palpite = int(input('qual é seu palpite? '))
tentativas = 1

if palpite > 10:
    print('\033[31mescolha somente entre 0 e 10.\033[m')

else:
    while palpite != rand:

        if palpite < rand:
            palpite = int(input('Mais... tente outra vez: '))
            tentativas += 1
        elif palpite > rand:
            palpite = int(input('Menos... tente outra vez: '))
            tentativas += 1

    print(f'\033[32mvoce acertou com {tentativas} parabens!!!\033[m')
    