horas = input("Que horas são?: ")

if horas.isdigit():
    horas = int(horas)
    if 0 <= horas <= 24:
        if 0 <= horas <= 11:
            print("Bom dia.")
        elif 12 <= horas <= 17:
            print("Boa Tarde.")
        elif 18 <= horas <= 23:
            print("Boa Noite.")
    else:
        print("Digite um número no intervalo [0 à 24]")
else:
    print(f"{horas} Não é um numero inteiro.")
