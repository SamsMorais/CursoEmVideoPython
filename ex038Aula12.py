n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
cores = {'amarelo': '\33[33m',
         'limpa': '\33[m'}
if n1 > n2:
    print(f'O número {cores["amarelo"]}{n1}{cores["limpa"]} é maior que o número '
          f'{cores["amarelo"]}{n2}{cores["limpa"]}.')
elif n2 > n1:
    print(f'O número {cores["amarelo"]}{n2}{cores["limpa"]} é maior que o número '
          f'{cores["amarelo"]}{n1}{cores["limpa"]}.')
else:
    print(f'O número {cores["amarelo"]}{n1}{cores["limpa"]} e o número '
          f'{cores["amarelo"]}{n2}{cores["limpa"]} tem valores iguais.')
