num = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        num += c
        cont += 1
print(f'Entre 1 e 500 existem {cont} números ímpares divisíveis por 3, e a soma entre eles da o valor {num}.')
