palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSOR', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
'PROGRAMADOR', 'FUTURO')

for c in palavras:
    print(f'\nNa palavra {c} temos',end='')
    
    if 'A'or 'E' or 'I' or 'O' or 'U' in c:
        print(c.count('A')* ' A ',end='')
        print(c.count('E')* ' E ',end='')
        print(c.count('I')* ' I ',end='')
        print(c.count('O')* ' O ',end='')
        print(c.count('U')* ' U ',end='')       




#for p in palavras:
#   print(f'\nNa palavra {p} temos ', end='')
#   for letra in p:
#   if letra.lower() in 'aeiou':
#       print (letra, end=' ')
