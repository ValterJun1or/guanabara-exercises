import random
x = input('Digite o nome de um aluno:')
y = input('Digite o nome de outro aluno:')
w = input('Digite o nome de outro aluno:')
z = input('Digite o nome de outro aluno:')
lista = [x, y, w, z]
aluno = random.choice(lista)
print('Entre {},{},{},{} o aluno que irá apagar o quadro é {}'.format(x, y, w, z, aluno))
