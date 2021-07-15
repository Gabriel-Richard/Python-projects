from random import randint
tupl = (0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9)
maior = 0
menor = 0


print (f'Os valores sorteados foram:',end='')
for c in range(0,5):
    
    n1 = randint(0, 10) 
    randnum = tupl[n1]
    print(end=''f' {randnum}' )
    
    if randnum > maior:
        maior = randnum
    if c == 1:
        menor = randnum
    elif randnum < menor:
        menor = randnum 
print(f'\nO maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')

#numeros = (randint (1,10),randint (1,10),randint (1,10),randint (1,10),randint (1,10))
#print ('Os valores sorteados são: ', end='')
#for n in numeros:
    #print(f'{n}'end='')
#print (f'O maior valor é {max(numeros)}')
#print (f'O menor valor é {min(numeros)}')
