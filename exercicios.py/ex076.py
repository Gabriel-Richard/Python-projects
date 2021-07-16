print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)

itens = (f'{"Lapis":.<40}R$:{" 1.75":>7}',f'{"Borracha":.<40}R$:{" 2.00":>7}',f'{"Caderno":.<40}R$:{" 15.90":>7}',
f'{"Estojo":.<40}R$:{" 25.00":>7}',f'{"Tranferidor":.<40}R$:{" 4.20":>7}',f'{"Compasso":.<40}R$:{" 4.99":>7}',
f'{"Mochila":.<40}R$:{" 120.32":>7}', f'{"Cananetas":.<40}R$:{" 22.30":>7}', f'{"Livro":.<40}R$:{" 34.90":>7}')

for c in itens:
    print(c)
print('-'*50)
