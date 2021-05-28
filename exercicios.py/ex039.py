from datetime import date
print('\033[36m~\033[m'*30)
print(' '*9,'\033[32mALISTAMENTO\033[m')
print('\033[36m~\033[m'*30)

print('''Defina o sexo que nasceu para iniciar. 
[ 1 ] \033[4mFeminino\033[m.
[ 2 ] \033[4mMasculino\033[m.''')

sx = input('\nColoque o numero correspondente a sua resposta: ').strip()
# tive de deixar sem especificar se é int ou str para que não houvesse a possibilidade de usar alguma
#  letra como resposta desse input. então usei o isnumeric para validar somente o 1 e 2.
if  sx == '1' and sx.isnumeric():

    print('\n\033[7;mVocê não tem como obrigatoriedade fazer o alistamento.\033[m')

elif sx == '2':
    ano = int(input('\n\033[4mDigite o ano de nascimento\033[m: '))

    data = date.today().year
    idade = data - ano

    if ano > data:
        print('\n\033[31mNOSSA VOCÊ VEIO DO FUTURO!!!\033[m então trate de voltar hehehe...')
    else:
        print('\nQuem nasceu em {} tem {} anos neste ano de {}.'.format(ano,idade,data))

        if idade > 18:
            print('Você ja deveria ter se alistado há {} anos.'.format(idade - 18))
            print('Seu alistamento foi em {}.'.format(data - (idade - 18)))
        elif idade < 18:
            print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
        else:
            print('VOCÊ TEM QUE SE ALISTAR IMEDIATAMENTE!!!')

else:
    print('\n\033[31mOpção inexistente. por favor escolha uma das opçoes acima!\033[m ')

print('\n', ' '*15, '\033[31mFIM\033[m')
