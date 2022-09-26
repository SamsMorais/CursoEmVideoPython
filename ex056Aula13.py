somaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
contmenor = 0
for c in range(1, 5):
    nome = str(input(f'Digite o nome da {c}º pessoa: ')).upper().strip()
    idade = int(input(f'Digite a idade da {c}º pessoa: '))
    sexo = str(input(f'Informe o sexo da {c}º pessoa: [M - Masculino / F - Feminino]')).upper()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        contmenor += 1
media = somaidade / 4
print(f'O homem mais velho se chama {nomemaisvelho} e tem {maioridadehomem} anos.')
print(f'A média das idades informadas é igual a {media} anos.')
print(f'Na lista existem {contmenor} mulheres com menos de 20 anos.')
