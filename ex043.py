print('='*35)
print(' '*10, 'TESTE DE IMC')
print('='*35)

print(' '*10,'TABELA DE IMC')
print('\033[36m v \033[m'*10, '\n')

print('''– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida\n''')

print('\033[36m ^ \033[m'*10, '\n')

peso = float(input('Qual seu peso? (Kg): '))
altura = float(input('Qual sua altura? (M):'))

imc = peso / altura**2

print('Seu IMC é de {:.1f}'.format(imc))

if imc <= 18.5:
    print('Você esta ABAIXO do \033[34mpeso\033[m.')
elif imc > 18.5 and imc < 25:
    print('Você está no peso \033[32mIDEAL.\033[m')
elif imc >= 25 and imc < 30:
    print('Você está com  \033[33mSOBREPESO.\033[m')
elif imc >= 30 and imc < 40:
    print('Você está com \033[35mOBESIDADE.\033[m')
elif imc >= 40:
    print('Você está com \033[31mOBESIDADE MÓRBIDA. CUIDADO!\033[m')
else:
    print('Veja se preencheu corretamente e tente preencher novamente.')