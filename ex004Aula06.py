n = input('Digite algo: ')
print('O tipo primitivo do caractere digiado é :', type(n))
print(f'Os caracteres digitados são alfabéticos? : {n.isalpha()}')
print(f'Os caracteres digitados são números? : {n.isnumeric()}')
print(f'Os caracteres digitados são alfanuméricos?: {n.isalnum()}')
print(f'Os caracteres digitados são maísculos?: {n.isupper()}')
print(f'Os caracteres digitados são minúsculos?: {n.islower()}')
print(f'Os caracteres digitados são espaços?: {n.isspace()}')
print(f'Os caracteres digitados são um título cammelcase?: {n.istitle()}') #capitalizada
print(f'Os caracteres digitados são imprimíveis?: {n.isprintable()}')
print(f'O Os caracteres digitados são decimais?: {n.isdecimal()}')
print(f'Os caracteres digitados constam somente alfanuméricos e underline?: {n.isidentifier()}')
print(f'Os caracteres digitados são digitos?: {n.isdigit()}')
print(f'Os caracteres digitados são Ascii?: {n.isascii()}')



