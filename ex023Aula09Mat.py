num = int(input('Informe um número: '))
m = num//1000
c = num//100 % 10
d = num//10 % 10
u = num % 10
print(f'O número informado possui {m} milhares')
print(f'O número informado possui {c} centenas')
print(f'O número informado possui {d} dezenas')
print(f'O número informado possui {u} unidades')
