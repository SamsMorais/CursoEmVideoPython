num = int(input('Digite um número inteiro: '))
div = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[33m', end=" ")
        div += 1
    else:
        print(f'\033[31m', end=" ")
    print(f'{c}', end=" ")
print(f'\n\033[mO número {num} tem {div} divisores')
if div == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')
