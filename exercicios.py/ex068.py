from random import randint
print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR?')
cont = 0
while True:
    print('-='*20)
    num = int(input('Diga um valor: '))
    pi = str(input('Par ou Impar? [P/I]'))
    pc = randint(0,10)
    soma = num + pc
    print('-'*40)
    if soma % 2 == 0:
        print(f'Voce jogo {num} e o computador {pc}. Total deu {soma} DEU PAR')
    elif soma % 2 == 1:
        print(f'Voce jogo {num} e o computador {pc}. Total deu {soma} DEU IMPAR')
    print('-'*40)
    if pi == 'p':
        if soma % 2 == 0:
            print('VOCE VENCEU!')
        else:
            print('VOCE PERDEU')
            break
    elif pi == 'i':
        if soma % 2 == 1:
            print('VOCE VENCEU!')
        else:
            print('VOCE PERDEU.')
            break        
    cont += 1
    print('Vamos jogar novamente...')
print(f'\033[31mGAMER OVER!\033[m voce venceu {cont} vezes')
    