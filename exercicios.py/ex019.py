import random
n1 = input('Primeiro  aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
alunos = (n1, n2, n3, n4)
print('Aluno escolhido foi: {}'.format(random.choice(alunos)))
# lista = [n1, n2 n3, n4]
# escolhido = random.choice(lista)