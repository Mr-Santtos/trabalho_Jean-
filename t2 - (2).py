while True:
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if senha == nome:
        print("Erro: A senha não pode ser igual ao nome de usuário.")
    else:
        print("Usuário e senha registrados com sucesso.")
        break
