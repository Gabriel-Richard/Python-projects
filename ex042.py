print('\033[36m-=-\033[m'*15)
print(' '*10, 'ANALIZADOR DE TRIÃNGULOS')
print('\033[36m-=-\033[m'*15,'\n')
primeiro = float(input('Primeiro seguimento: '))
segundo = float(input('Segundo seguimento: '))
terceiro = float(input('Terceiro seguimento: '))

print('\n','\033[35m*\033[m'*40, '\n')

if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < segundo + primeiro:
    if primeiro == segundo == terceiro:
        print('Pode se formar um triangulo \033[32mEQUILATERO\033[m.')
    elif primeiro == segundo != terceiro or segundo == terceiro != primeiro or terceiro == primeiro != segundo:
        print ('Pode se formar um triangulo \033[33mISOCELES\033[m')
    elif primeiro != segundo != terceiro or segundo != terceiro != primeiro or terceiro != primeiro != segundo:
        print('Pode se formar um triangulo \033[35mESCALENO\033[m.')
#         elif primeiro != segundo != terceiro != primeiro. guanabara.
else:
    print('\n\033[31mNÃO PODE SE FORMAR UM TRIANGULO!\033[m')

print('\n','\033[35m*\033[m'*40)