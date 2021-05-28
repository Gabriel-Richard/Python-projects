print('\033[37m~\033[m'*43)
print(' '*15,'MEDIA DO ALUNO')
print('\033[37m~\033[m'*43)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('\n\033[31mREPROVADO.\033[m')
elif media >= 5 and media < 6.9:
    print('\n\033[34mRECUPERAÇÃO\033[m')
else:
    print('\n\033[32mAPROVADO.\033[m')
print(media)
