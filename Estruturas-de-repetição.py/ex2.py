nome = str(input('Digite o nome do usuario: '))
senha = str(input('Digite sua senha: '))

while nome == senha:
    print(' '*25,'''\033[31mERRO\033[m
\033[7;30mNão é permitido que o nome do usuario e senha sejam iguais.\033[m\n''')

    nome = str(input('Digite o nome do usuario novamente: '))
    senha = str(input('Digite a senha novamente: '))

print('\033[32mparabéns, login concluido!\033[m ')

