n1 = int(input('Informe o número desejado: '))
n2 = int(input('Informe o número desejado: '))
n3 = int(input('Informe o número desejado: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n2
if n1 < n2 and n1 < n3:
    menor = n1
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O maior número informado foi {maior}!')
print(f'O menor número informado foi {menor}!')
