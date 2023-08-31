numero = input("Digite o numero: ")

if numero.isdigit():
    numero = int(numero)

    if numero % 2 == 0:
        print(f"{numero} é PAR.")
    else:
        print(f"{numero} é IMPAR")
else:
    print(f"{numero} Não é um numero inteiro")
