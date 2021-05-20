media = 0
maioridade = 0
qf = 0
nm = str()

for p in range (1,5):
    print('------ ANALIZANDO A {}ª PESSOA ------'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).upper()
    media += idade

    if sexo == 'M':
         if idade > maioridade:
            maioridade = idade
            nm = nome

    if sexo == 'F':
        if idade < 20:
            qf += 1

print('A media de idade do grupo é de {}'.format(media / 4))
print('O homem mais velho do grupo tem {} anos e se chama {} '.format(maioridade, nm ))
print('Ao todo são {} com menos de 20 anos.'.format(qf))