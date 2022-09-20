from math import hypot
catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdj = float(input('Digite o comprimento do cateto Adjacente: '))
hipo = hypot(catOposto , catAdj)
print(f'O valor da hipotenusa é {(hipo) :.2f}')