total = contV = mv = 0
nomeMB = ' '
while True:
    print('-'*20)
    print('LOJA SUPER BARATÃO')
    print('-'*20)

    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$'))
    total += valor 
    
    if valor >= 1000: 
        contV +=1
    
    if mv == 0 or valor < mv:
        mv = valor 
        nomeMB = nome       
   
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('-'*10,'FIM DO PROGRAMA','-'*10)
print(f'''O valor total foi de {total:.2f}
temos {contV} custando mais de 1.000.00
O produto mais barato foi {nomeMB} que custa R${mv:.2f}''')
