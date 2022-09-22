num = int(input('Digite um número inteiro para converter: '))
cores = {'vermelho': '\033[31m',
         'verde': '\033[32m',
         'limpa': '\033[m'}
print(f"""Escola a base de conversão:'
      [1] Converter para {cores["vermelho"]}Binário{cores["limpa"]}'
      [2] Converter para {cores["vermelho"]}Octal{cores["limpa"]}'
      [3] Converter para {cores["vermelho"]}Hexadecimal{cores["limpa"]}""")
base = int(input('Digite sua opção: '))
if base == 1:
    print(f'O número {cores["verde"]}{num}{cores["limpa"]} convertido em Binário é {cores["verde"]}{bin(num)[2:]}')
elif base == 2:
    print(f'O número {cores["verde"]}{num}{cores["limpa"]}  convertido para Octal é {cores["verde"]}{oct(num)[2:]}')
elif base == 3:
    print(f'O número {cores["verde"]}{num}{cores["limpa"]}  convertido para Hexadeximal é {cores["verde"]}'
          f'{hex(num)[2:]}'f'')
else:
    print('Digite um número válido ( 1-3 )')
