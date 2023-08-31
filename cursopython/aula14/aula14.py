frase = 'O Rato roeu a roupa do rei da Roma'

tamanhoFrase = len(frase)
contador = 0
novaString = ''

while tamanhoFrase > contador:
    letra = frase[contador]
    if letra == 'r' or letra == 'R':
        novaString += '___'
    else:
        novaString += letra
    contador += 1
print(novaString)
