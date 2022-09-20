num = str(input('Digite um número de 0 a 9999: '))
s = '0000' + num
print(f'O número informado possui {s[-4]} milhares')
print(f'O número informado possui {s[-3]} centenas')
print(f'O número informado possui {s[-2]} dezenas')
print(f'O número informado possui {s[-1]} unidades')