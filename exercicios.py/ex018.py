import  math
n1 = float(input('digite um angulo: '))
seno = math.sin(math.radians(n1))
print('O angulo de {} tem o SENO de {:.2f} '.format(n1, seno))
cosseno = math.cos(math.radians(n1))
print('O angulo de {} tem o COSSENO de {:.2f} '.format(n1, cosseno))
tangente = math.tan(math.radians(n1))
print('O angulo de {} tem a TANGENTE de {:.2f} '.format(n1, tangente))


