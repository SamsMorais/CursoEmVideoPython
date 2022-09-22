valor = float(input('Informe o valor da compra: R$'))
pagamento = int(input("""Informe a forma de pagamento:
[1] Dinheiro ou cheque
[2] À vista no Cartão
[3] Em até 2x no Cartão
[4] 3x ou mais no Cartão  :"""))
if pagamento == 1:
    desconto = valor * 10/100
    valor = valor - desconto
    print(f'O seu desconto é de {desconto}R$ e o valor total da compra {valor}R$.')
elif pagamento == 2:
    desconto = valor * 5/100
    valor = valor - desconto
    print(f'O seu desconto é de {desconto}R$ e o valor total da compra {valor}R$.')
elif pagamento == 3:
    valor = valor
    parcela = valor / 2
    print(f'O valor de sua compra é {valor} e as parcelas de sua compra serão 2x {parcela} R$.')
elif pagamento == 4:
    valor = valor + valor * 20/100
    parcela = valor / 3
    print(f'O valor de sua compra é {valor} e as parcelas de sua compra serão 3 x {parcela} R$.')
else:
    print('Opção inválida, por favor altere o modo de pagamento')
