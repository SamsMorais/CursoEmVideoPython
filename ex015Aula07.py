km = float(input('Informe a quilometragem percorrida com o carro alugado : '))
dias = int(input('Informe o quantitativo de dias de aluguel do carro : '))
preco = (dias * 60) + (km * 0.15)
print(f'O Valor total do aluguel é : R${preco :.2f}')
