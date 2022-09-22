valor = float(input('Informe o valor da casa a ser adquirida.: R$ '))
salario = float(input('Informe o salário do comprador.: R$ '))
anospag = int(input('Informe a pretensão quantidade de anos que a casa será quitada.: '))
prestMensal = valor / (anospag * 12)
cores = {'vermelho': '\033[31m',
         'verde': '\033[32m',
         'limpa': '\033[m'}
if prestMensal >= salario * 30/100:
    print(f'O empréstimo foi {cores["vermelho"]} Negado {cores["limpa"]}. A prestação de {cores["vermelho"]}'
          f' {prestMensal:.2f}{cores["limpa"]}R$ excede 30% do salário.')
else:
    print(f'O empréstimo foi previamente {cores["verde"]} Aceito! {cores["limpa"]} O valor da parcela será '
          f'{cores["verde"]}{prestMensal:.2f}{cores["limpa"]} R$! Parabéns por a aquisição')
