print('======= LOJAS BABYLU ========\n')

valor = input('Valor das compras: ')

if valor.isalpha():
    print('\n\033[31mApenas caracteres NUMERICOS são aceitos!\033[m')
else:
    valor = float(valor)

    print('\n','-'*30,'\n')
    print('FORMAS DE PAGAMENTOS.')

    print('''
[ 1 ] á vista dinheiro/cheque 
[ 2 ] á vista cartão.
[ 3 ] 2x no cartão.
[ 4 ] 3x no cartão ou mais no cartão.\n''')

    pagamento = int(input('Digite a forma de pagamento: '))

    if pagamento == 1:
        desc = valor / 10
        print('Sua compra de R${} vai custar R${} no final'.format(valor, valor-desc))
    elif pagamento == 2:
        desc = (valor * 0.05 - valor)* -1
        print('sua compra de R$ {} vai custar R$ {} no final'.format(valor, desc ))
    elif pagamento == 3:
        print('\nSua compra será em 2x de R${:.2f} SEM JUROS.'.format(valor / 2))
        print('O valor total a pagar é R${}',format(valor))
    elif pagamento == 4:
        par = int(input('\n''Quantas parcelas: '))
        if par == 1 or 2:
            print('\n\033[31mParcela invalida para essa opção.\033[m\n')
        else:
            x = (valor * 0.20 + valor) / par
            print('\nSua compra será parcela em {}x de R${:.2f} COM JUROS.'.format(par, x))
            print('Sua compra de R${:.2f} com juros sera de R${:.2f} no final.\n'.format(valor,valor * 0.20 + valor ))
    else:
        print('\n\033[7;31mOpções validas somentes 1, 2, 3 e 4. \033[m\n')

print('-'*30)
