from random import randint
num = randint(0, 5)
n = int(input('Entre 0 e 5, adivinhe o número escolhido pelo computador: '))
if n == num:
    print('UAU! Você venceu!')
else:
    print(f'BOOO! Você perdeu! O número sorteado foi {num}!')

#print(f'Vencedor!' if n == num else 'Perdedor!')   --- condição simplificada

