from random import choice
a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite o nome do aluno: '))
a3 = str(input('Digite o nome do aluno: '))
a4 = str(input('Digite o nome do aluno: '))
list =[a1,a2,a3,a4]
sort = choice(list)
print(f'O aluno sorteado foi: {sort}')