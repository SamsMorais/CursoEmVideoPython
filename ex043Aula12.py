altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))
imc = peso / (altura * altura)
if imc <= 18.5:
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso ideal.')
elif 18.5 < imc <= 25:
    print(f'Seu IMC é {imc:.2f} e você está no peso ideal.')
elif 25 < imc <= 30:
    print(f'Seu IMC é {imc:.2f} e você está com sobrepeso.')
elif 30 < imc <= 40:
    print(f'Seu IMC é {imc:.2f} e você está Obeso.')
else:
    print(f'Seu IMC é {imc:.2f} e você está com Obesidade Mórbida')
