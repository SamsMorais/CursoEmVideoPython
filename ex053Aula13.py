frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = ''
for letra in range(len(juntos)-1, -1, -1):
    inverso += juntos[letra]
if inverso == juntos:
    print(f'A frase ao contrário é {inverso}, se caracterizando como um palíndromo!')
else:
    print(f'A frase ao contrário é {inverso}, e não se caracteriza como um palíndromo')
