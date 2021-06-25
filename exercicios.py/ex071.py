print('='*30)
print('{: ^30}'.format('BANCO CV'))
print('='*30)
notas50 = notas20 = notas10 = notas1 = 0
valor = int(input('Que valor você quer sacar: '))
while True:
    while valor >= 50: 
        valor -= 50
        notas50 += 1
    while valor >= 20:
        valor -= 20
        notas20 += 1
    while valor >= 10:
        valor -= 10
        notas10 += 1
    while valor > 0:
        valor -= 1
        notas1 += 1
    if valor == 0:
        break
if notas50 > 0:
    print(f'Total de {notas50} Cedulas de R$50')
if notas20 > 0: 
    print(f'total de {notas20} Cedulas de R$20')
if notas10 > 0:
    print(f'total de {notas10} Cedulas de R$10')
if notas1 > 0:
    print(f'total de {notas1} Celudas de R$1')