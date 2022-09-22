from datetime import date
nascimento = int(input('Informe o ano de seu nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento
carencia = 18 - idade
excedente = idade - 18
cores = {'amarelo': '\33[33m',
         'limpa': '\033[m'}
if idade < 18:
    print(f'Sua idade é {cores["amarelo"]}{idade}{cores["limpa"]} e faltam {cores["amarelo"]}'
          f'{carencia}{cores["limpa"]} anos para se alistar.')
elif idade == 18:
    print(f'Sua idade é {cores["amarelo"]}{idade}{cores["limpa"]}e está na hora de se alistar.')
else:
    print(f'Sua idade é {cores["amarelo"]}{idade}{cores["limpa"]} e já passou '
          f'{cores["amarelo"]}{excedente}{cores["limpa"]} anos do tempo do alistamento.')
