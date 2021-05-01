n1 = input('digite seu nome: ')
print('''====ANALISANDO SEU NOME====''')
print('Seu nome em maiusculo é:',n1.upper())
print('seu nome em minusculo é:',n1.lower())
print('seu nome tem ao todo tem {} letras. '.format(len(n1.replace(' ',''))))
# print('seu nome tem ao todo tem {} letras. '.format(len(n1) - n1.count(' '))) #guanabara O.P
n2 = n1.split( )
n3 = n2[0]
print('Seu priemiro nome é {} e tem {} letras.'.format(n3, len(n3)))