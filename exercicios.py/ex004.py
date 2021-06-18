a = input('digite algo: ')
print('{} \ntem espaço? {} \nÉ um numero? {} \nÉ alfabetico? {} \nÉ alfanumerico? {} \nEsta em maiusculo? {} \nEsta em minusculo? {} \nEsta capitalizado? {}'
      .format( type, a.isspace(), a.isnumeric(), a.isalpha(), a.isalnum(), a.isupper(), a.islower(), a.istitle() ))
# 'a' é o nome dado d mim para a variavel. mas nesse caso ele é um objeto.
