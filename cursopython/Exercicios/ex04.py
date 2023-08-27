idade = int(input("Digite a idade: "))

if idade < 16:
    print("Não eleitor")
elif 18 <= idade < 65:
    print("Eleitor Obrigatório")
elif (16 <= idade <= 18) or idade > 65:
    print("Eleitor Facultativo")
