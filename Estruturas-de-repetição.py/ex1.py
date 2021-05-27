nota = float(input('Insira uma nota de 0 a 10: '))
while nota > 10:
    print('\033[31mValor de nota invalido.\033[m')
    nota = float(input('Digite novamente: '))
else:
    print(f'\033[32mA nota que vc esolheu foi: {nota} Obrigado!\033[m\nFIM. ')    
    