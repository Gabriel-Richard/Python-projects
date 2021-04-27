n1 = int(input('\033[36mPrimeiro numero: \033[m'))
n2 = int(input('\033[36mSegundo numero: \033[m'))

print('\033[35m~\033[m'*28)

if  n1 > n2:
    print('O PRIMEIRO numero é maior!')
elif n2 > n1:
    print('O SEGUNDO numero é maior')
else:
    print('OS DOIS numeros são inguais.')

print('\033[35m~\033[36m'*28)