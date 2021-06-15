n1 = soma = 0
contador = 0

n1 = int(input('Digite um numero [999 para parar]: '))

while n1 != 999:
    soma += n1
    contador += 1
    n1 = int(input('Digite um numero [999 para parar]: '))
print('=-'*30)
print(f'Voce digitou \033[36m{contador}\033[m numeros e a soma entre eles foi \033[31m{soma}\033[m. ')
print('=-'*30)
