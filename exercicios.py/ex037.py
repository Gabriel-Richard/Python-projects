n = int(input('\033[36mDigite um valor: \033[m'))

print('Escolha uma das bases para a converção.')
print('\033[32m[ 1 ] Converter para BINARIO.\033[m')
print('\033[35m[ 2 ] Converter para OCTAL.\033[m')
print('\033[34m[ 3 ] converter para HEXADECIMAL.\033[m')

opcao = int(input('\033[4mSua opção\033[m :'))

if opcao == 1:
    print('{}\033[32m convertido para BINARIO é igual a:\033[m {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{}\033[35m convertido para OCTAL é igual a:\033[m {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{}\033[34m convertido para HEXADECIMAL é igual a:\033[m {}'.format(n, hex(n)[2:]))
else:
    print('-=-'*9)
    print('\033[31mOpção invalida!!!\033[m')
    print('-=-'*9)
    