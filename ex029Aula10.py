velocidade = float(input('Informe a velocidade do carro : KM '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Multado! A velocidade informada está acima do limite permitido, o valor da multa será {multa}R$!')
else:
    print('A velocidade está dentro dos limites estabelecidos, continue a dirigir com segurança!')
