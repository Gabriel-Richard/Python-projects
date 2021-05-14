print('='*25, '\n')
print('10 TERMOS DE UMA PA \n')
print('='*25, '\n')

pt = int(input('Primeiro termo: '))
rz = int(input('Digite a Razão: '))
dc = pt + (10 - 1) * rz

for c in range (pt , dc + rz , rz ):
    print(c, end=' -> ')

print('\033[31mACABOU')
