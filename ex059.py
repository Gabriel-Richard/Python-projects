from time import sleep
pv = int(input('Primeiro valor: '))
sv = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:

    print('''\nEscolha um apção para continuar.
     [ 1 ] Soma.
     [ 2 ] Multiplicar.
     [ 3 ] Maior. 
     [ 4 ] Novos numeros. 
     [ 5 ] Sair do programa. \n''')

    opcao = int(input('>>>> Qual é a sua opção: '))

    if opcao == 1:
        print(f'\nA soma entre {pv} + {sv} é {pv + sv}. ')

    elif opcao == 2:
        print(f'\nO resultado de {pv} x {sv} é {pv * sv}.')

    elif opcao == 3:
        if pv > sv:
            print(f'\nEntre {pv} e {sv} o maior valor é {pv}. ')
        else:
            print(f'\nEntre {pv} e {sv} o maior valor é {sv}. ')

    elif opcao == 4:
        pv = int(input('primeiro valor: '))
        sv = int(input('Segundo valor: '))
    print('-=' * 20)
    sleep(2)
    
print('\nFinalizando programa...')
sleep(2)
print('FIM')