sexo = str(input('Informe seu sexo. [F/M]: ')).strip().upper()[0]

while sexo != 'F' and sexo != 'M':
    sexo = str(input('\n\033[31mDados invalidos.\033[m Por favor, informe seu sexo com [F/M]: ')).strip().upper()[0]

print(f'\033[32mSexo {sexo} registrado com sucesso.\033[m')
