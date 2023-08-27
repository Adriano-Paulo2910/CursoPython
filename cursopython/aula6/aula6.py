import datetime

nome = "Adriano Paulo"
idade = 23
altura = 1.65
peso = 60.5
imc = peso / (altura ** 2)

# Obter a data atual
dataAtual = datetime.date.today()

# Obter o ano atual apartir da data atual
anoAtual = dataAtual.year

anoNascimento = anoAtual - idade

print(f"{nome}, tem {idade} anos de idade, tem {altura} de altura e pesa {peso}kg.")
print(f"O seu IMC é {imc:.2f}")
print(f"{nome} nasceu em {anoNascimento}.")
