print('-='*10)
print('Gerador de PA')
print('-='*10)

pt = int(input('primeiro termo: '))
rz = int(input('Razão da PA: '))
contador = 0
pa = pt - rz

while contador != 10:
    pa += rz
    contador += 1
    print(pa, end= '->')

print('\033[31mFIM\033[m')
