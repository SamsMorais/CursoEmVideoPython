nome = str(input('Informe o nome da cidade: '))
nome = nome.strip().lower().split()
comp = {nome[0] == 'santo'}
print(f'O nome da cidade inicia com Santo? {comp}')



