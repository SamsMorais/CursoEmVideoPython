s1 = float(input('Informe o primeiro segmento de reta: '))
s2 = float(input('Informe o segundo segmento de reta: '))
s3 = float(input('Informe o terceiro segmento de reta: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos poderão formar um triângulo', end=" ")
    if s1 == s2 == s3:
        print('Equilátero.')
    if s1 == s2 != s3 or s1 == s3 != s2 or s2 == s3 != s1:
        print('Isósceles.')
    if s1 != s2 != s3:
        print('Escaleno.')
else:
    print('Os segmentos não poderão formar um triângulo!')
