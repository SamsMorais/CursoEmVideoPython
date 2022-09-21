distancia = float(input('Informe a distância da viagem em km: KM '))
if distancia <= 200:
    passagem = distancia * 0.50
    print(f'Sua viagem terá {distancia}Km, e o valor da passagem será {passagem}! Boa viagem!')
else:
    passagem = distancia * 0.45
    print(f'Sua viagem terá {distancia}Km, e o valor da passagem será {passagem}! Boa viagem!')
