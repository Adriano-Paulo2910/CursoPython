peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura * altura)

print(f"IMC: {imc:.2f}")

if imc < 20:
    print("Abaixo do peso.")
elif imc >= 20 and imc <= 25:
    print("Peso Normal")
elif imc <= 30:
    print("Sobre Peso")
elif imc <= 40:
    print("Obeso")
elif imc > 40:
    print("Obeso Mórbido")
