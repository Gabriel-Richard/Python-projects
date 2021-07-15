nuns = (int(input('Digite um numero: ')),int(input('Digite outro numero: ')),int(input('Digite mais um numero: ')),int(input('Digite o ultimo: numero: ')))
print (f'Você digitou os valores {nuns}')
print (f'O valor 9 apareceram {nuns.count(9)} vezes')

try:
    nuns.index(3) == True
    print (f'O valor 3 apareceu na {nuns.index(3)+1}° posição.')
except ValueError:
    print(f'O valor 3 não apareceu em nenhuma posição.')

print ('Os valores pares digitados foram: ', end='')

for c in range (0,4):
    if nuns[c] % 2 == 0:
        print (end=' ' f'{nuns[c]}')
