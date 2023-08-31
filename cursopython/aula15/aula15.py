"""
nome = 'Adriano'

for letra in nome:
    print(letra, end='')
"""
texto = 'Adriano Paulo'
apagaLetra = ''
for letra in texto:
    if letra == 'o':
        continue
    elif letra == 'a':
        apagaLetra = apagaLetra + '?'
    else:
        apagaLetra += letra
print(apagaLetra)

