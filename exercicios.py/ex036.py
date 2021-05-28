valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o Salario do comprador: R$'))
anos = float(input('Em quantos anos sera pego: '))

vano = valor/anos
prestacao = vano / 12

print('\033[4mPara pagar uma casa de R$:{} em {:.0f} anos a prestação sera de R${:.2f}\033[m'.format(valor, anos, prestacao))

if prestacao < salario * 0.30:
    print('\033[4mSeu emprestimo foi\033[m \033[36;mAPROVADO \033[m!')
else:
    print('\033[4mSeu imprestimo foi\033[m \033[31;mNEGADO\033[m')
