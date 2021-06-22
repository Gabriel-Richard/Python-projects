
conti = 0
conts = 0
contf = 0

while True:
    print('-'*40)
    print('CADASTRE UMA POSSOA')
    print('-'*40)

    idade = int(input('Idade: '))
    
    sexo= ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:  [M/F]')).strip().upper()[0]
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    
    if idade >= 18: 
        conti+=1 
    if sexo in 'Mm':
        conts +=1
    if sexo in 'Ff' and idade < 20:
        contf+=1

    if resposta in 'Nn':
        break
print(f'''Total de pessoas com mais de 18 anos: {conti}
        Ao todo temos {conts} Homens cadastrados
        E temos {contf} mulheres com menos de 20 anos. ''')