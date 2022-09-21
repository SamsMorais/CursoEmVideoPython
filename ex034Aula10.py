salario = float(input('Informe o seu salário: '))
if salario >= 1250:
    novosalario = salario * 1.10
    print(f'O valor do salário com aumento será {novosalario}R$!')
else:
    novosalario = salario * 1.15
    print(f'O valor do salário com aumento será {novosalario}R$!')
