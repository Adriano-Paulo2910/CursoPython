import datetime

nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))

dataAtual = datetime.date.today()
anoAtual = dataAtual.year
anoNascimento = anoAtual - idade

print(f"{nome} tem {idade} anos de idade", type(nome), type(idade))
print(f"Nasceu em: {anoNascimento}")
