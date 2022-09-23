pri = int(input('Digite o primeiro termo da P.A. : '))
raz = int(input('Digite a razão da P.A. :'))
dec = pri + 10 * raz
for c in range(pri, dec, raz):
    print(c, end=", ")
print('Fim!')
