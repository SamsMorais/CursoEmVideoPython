maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Informe o peso da {pessoa}º pessoa:KGs '))
    if pessoa == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f' O maior peso da lista é {maior}Kgs, enquanto o menor é {menor}Kgs')
