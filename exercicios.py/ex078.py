lista = []

for c in range (0, 5):
    n1 = int(input(f'Digite um valor para a posição {c}: '))
     
    lista.append(n1)    

for x in range (0, 5):
    if lista [x] == max(lista):
       n2 = x

for z in range (0, 5):
    if lista [z] == min(lista):
        n3 = z

print ('-='*20)
print (f'Voce digitou os valores {lista}')
print (f'O maior valor digitado foi {max(lista)}. Nas posições {lista.index(max(lista))}... {n2}...')
print (f'O menor valor digitado foi {min(lista)}. Nas posições {lista.index(min(lista))}... {n3}...')

