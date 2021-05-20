pesoAt = 0
pminimo = 500

for c in range (1,6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if peso > pesoAt:
        pesoAt = peso

    if peso < pminimo:
        pminimo = peso

print('o maior peso é {}kg'.format(pesoAt))
print('O menor peso é de {}kg'.format(pminimo))