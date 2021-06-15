n1 = soma =0
cont = 1

n1 = int(input('Digiteb um numero: '))
resposta = str(input('Quer continuar ? [S/N]')).upper()
maior = n1
menor = n1

while resposta == 'S':
    n1 = int(input('Digiteb um numero: '))
    resposta = str(input('Quer continuar ? [S/N]')).upper()
    cont += 1
    soma += n1

    if n1 < maior:
        maior = n1

    if n1 > menor:
        menor = n1
print(f'Voce digitou {cont} numeros e a média foi de {soma / cont} ')
print(f'O maior valor foi {menor} e o menor valor foi {maior} ')
