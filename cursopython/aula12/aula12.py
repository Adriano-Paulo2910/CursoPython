"""

numero1 = 12
numero2 = 13

divisao = numero1 / numero2

print("{:.2f}" .format(divisao))

nome = 'Adriano'
sobrenome = 'Paulo'

nomeFormatado = '{1:#^20}'.format(nome, sobrenome)
print(nomeFormatado)
"""

# Fatiamento de String
nome = 'Paulo Cadeth Adriano'
print(nome[::])
