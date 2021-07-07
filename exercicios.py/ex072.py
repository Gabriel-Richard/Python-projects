listanum = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True: 
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <=20:
        print(f'Você digitou o numero {listanum[num]}')
        resposta = str(input('\nQuer continuar? [S/N]: ')).strip().upper()
        if resposta == 'N':
            break       
    print('tente novamente.', end=' ')

