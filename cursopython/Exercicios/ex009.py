nome = input("Digite um nome: ")

if not nome.isdigit():
    qtdCaractere = len(nome)
    if qtdCaractere <= 4:
        print("Seu nome é curto.")
    elif qtdCaractere <= 6:
        print("Seu nome é normal.")
    else:
        print("Seu nome é muito grande.")
else:
    print("Isto não é um nome. São apenas números...")
