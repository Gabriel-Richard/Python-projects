cont = 0

while True:
    print('-'*40)

    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break

    while True:
        if cont == 10: 
            break
        cont += 1
        print(f'{num} x {cont} = {num * cont}')
    cont = 0         
print('PROGRAMA DE TABUADA ENCERRADO. volte sempre!')    
    