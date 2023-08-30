usuario = str(input("Usuario: "))
senha = int(input("Senha: "))

usuarioBD = 'Paulo'
senhaBD = 12345

if usuarioBD == usuario and senha == senhaBD:
    print("Você está logado.")
else:
    print("Não existe na Base de Dados")
