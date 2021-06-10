print('=-'*25)
print(f'{"Sequencia de fibonacci": ^50}')
print('=-'*25, '\n')

termos = int(input('Quantos termos voce quer mostrar: '))
controle = 0
fibonacci = 0
n1 = 0
n2 = 1

print(n1, '->',  n2, end=' -> ')
while controle != termos - 2:
    controle += 1
    fibonacci = n1 + n2
    n1 = n2
    n2 = fibonacci
    print(fibonacci, end=' -> ')
print('FIM')
print('\n','=-'*25)
