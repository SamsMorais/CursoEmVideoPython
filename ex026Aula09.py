frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A, aparece {frase.count("A")} vezes na frase')
print(f'A primeira que a letra A aparece é no índice {frase.find("A")+1} e a última é no índice {frase.rfind("A")+1}')
