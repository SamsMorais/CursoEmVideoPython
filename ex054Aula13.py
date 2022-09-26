from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    data = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    idade = atual-data
    if idade > 21:
        maior += 1
    else:
        menor += 1
print(f' Ao analisar o grupo, contabilizamos {maior} maiores de idade e {menor} menores de idade.')
