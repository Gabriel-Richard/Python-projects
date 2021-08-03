lista = []

contMx = 0
contMn = 0 
for c in range (0, 5):
    n1 = int(input(f'Digite um valor para a posição {c}: '))
    
   #if contMx == 0:
    #    contMx = n1 
    #else:
     #   contMx 


    #print(contMx)     
    lista.append(n1)    


valorMaximo = lista.index(max(lista))


print ('-='*20)
print (f'Voce digitou os valores {lista}')
print (f'O maior valor digitado foi {max(lista)}. Nas posiçoes {lista.index(max(lista))}... {valorMaximo}...')
print (f'O menor valor digitado foi {min(lista)}.')

print (lista.reverse = True)