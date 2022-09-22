from datetime import date
nascimento = int(input('Informe o ano de nascimento do nadador: '))
anoatual = date.today().year
idade = anoatual - nascimento
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')
