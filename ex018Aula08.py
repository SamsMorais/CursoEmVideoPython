import math
ang = float(input('Digite o ângulo: '))
rad = math.radians(ang)
cos = math.cos(rad)
sen = math.sin(rad)
tan = math.tan(rad)
print(f'O cosseno do ângulo {ang}º é: {cos :.4f} \nO seno do ângulo {ang}º é:{sen :.4f}')
print(f'A tangente do ângulo {ang}º é {tan :.4f}')
