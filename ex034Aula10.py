salario = float(input('Informe o seu salário: '))
cores = {
         'vermelho': '\033[31m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'branco': '\033[30m',
         'roxo': '\033[35m',
         'verde': '\033[32m',
         'ciano': '\033[36m',
         'limpa ': '\033[m',
         'preto e branco': '\033[7;30;m', }
if salario >= 1250:
    novosalario = salario * 1.10
    print(f'O valor do salário com aumento será {cores["verde"] } {novosalario :.2f}R$!')
else:
    novosalario = salario * 1.15
    print(f'O valor do salário com aumento será {cores["vermelho"]} {novosalario :.2f}R$!')
