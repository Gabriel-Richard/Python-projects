from datetime import date
print('\033[36m+\033[m'*40)
print('TABELA DE CLASSIFICAÇÕES DAS NATAÇÃO')
print('\033[36m+\033[m'*40)
ano = int(input('\nAno de nascimento: '))

data = date.today().year
idade = data - ano

print('O atleta tem {}'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM.')

elif idade > 9 and idade <=14:
    print('Classificação: INFANTIL.')

elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR.')

elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR.')

elif idade > 25 and idade <= 120:
    print('Classificação: MASTER.')

else:
    print('Inexistente. Digite novamente...')