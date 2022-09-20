from random import shuffle
a1 = (input('Digite o nome do aluno: '))
a2 = (input('Digite o nome do aluno: '))
a3 = (input('Digite o nome do aluno: '))
a4 = (input('Digite o nome do aluno: '))
l = [a1,a2,a3,a4]
shuffle(l)
print(f'A ordem de alunos que irão apresentar o trabalho é: {l}')