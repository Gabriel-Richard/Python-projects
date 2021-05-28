nome = str(input('Digite o nome do usuario: '))
senha = input('Digite sua senha: ')
while nome == senha:
    print('\033[31mNão é permitido que use nome do usuario e senha iguais.\033[m')
    