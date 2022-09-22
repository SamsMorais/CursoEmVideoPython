from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
player = int(input("""Escolha:
[0] Pedra
[1] Papel
[2] Tesoura  :  """))
pc = randint(0, 2)
print(f'O computador escolheu {itens[pc]}')
print(f' Você escolheu {itens[player]}')
if player == pc:
    print('Empate!')
elif player == 0:
    if pc == 1:
        print('Derrota')
    if pc == 2:
        print('Vitória')
elif player == 1:
    if pc == 0:
        print('Vitória')
    if pc == 2:
        print('Derrota')
elif player == 2:
    if pc == 0:
        print('Derrota')
    if pc == 1:
        print('Vitória')
else:
    print('Jogada Inválida')
