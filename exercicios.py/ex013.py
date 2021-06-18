n1 = float(input('Digite o salario do funcionario: '))
n2 = float(input('digite o valor de desconto: '))
r = n2*n1
print('o salario atual do funcionario é de:{} \ncom reajuste de {}% é = {}'.format(n1, n2, r/100+n1))
#                                                                      {:.2f}
# variavel vezes % dividido por 100 + variavel