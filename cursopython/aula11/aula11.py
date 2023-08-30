num1 = input("Numero 1: ")
num2 = input("Numero 2: ")


if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    soma = num1 + num2

    print(f"Resul : {soma}")
else:
    print("Não foi possivel converter...")
