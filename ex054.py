from datetime import date
data = date.today().year

novo = 0
velho = 0

for c in range (1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    idade = data - ano
    if idade >= 18:
        velho += 1
    else:
        novo += 1

print('Ao todo tivemos {} maiores de idade'.format(velho))
print('E também tivemos {} pessoas menores de idade.'.format(novo))