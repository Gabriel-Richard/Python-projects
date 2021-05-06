n1 = str(input('Digite seu nome completo: ')).strip()
print ('prazer em te conecer!')
n2 = n1.split()
print ('Seu primeiro nome é: {}'.format(n2 [0]))
print ('Seu ultimo nome é: {}'.format(n2 [-1]))
# outro modo
# print ('Seu ultimo nome é: {}'.format(n2 [len(n2)-1]))