frase = str(input('Digite uma frase: ')).strip()
# fc = len(frase) - frase.count(' ')
fs = frase.replace(' ','')
cont = 0
for c in range (0, len(fs)):
    if fs [c] == fs [-c-1]:
        cont += 1

if cont == fs:
    print('O inverso de {} é {}'.format(frase, frase[::-1]))
    print('Temos um PALINDROMO')
else:
    print('O inverso de {} é {}'.format(frase, frase[::-1]))
    print('A frase digitada não é um PALINDROMO')
    