acumulador = 0
sdt = 0
for c in range (1,501,2):
    if c % 3 == 0:
        sdt = sdt + 1
        acumulador = acumulador + c
print('A soma de todos os {} valores é de {}'.format(sdt, acumulador))