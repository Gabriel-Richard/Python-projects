print('Gerador de PA')
print('-='*10 )

pt = int(input('Priemiro termo: '))
rz = int(input('Razão da PA: '))
pa = pt - rz
resposta = 1
contador = 0
n1 = 10

while resposta != 0:

    while contador != n1:
        pa+= rz
        contador += 1

        print(pa, end=' -> ')
    print('PAUSA')

    resposta = int(input('Quantos termos voce quer mostrar a mais? '))
    n1 += resposta

print(f'progressão finalizada com {contador} termos mostrados  ')
