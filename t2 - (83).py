def copiar_arquivo(origem, destino):
    try:
        with open(origem, 'r', encoding='utf-8') as f_origem:
            conteudo = f_origem.read()
        with open(destino, 'w', encoding='utf-8') as f_destino:
            f_destino.write(conteudo)
    except FileNotFoundError:
        print(f"Erro: Arquivo de origem '{origem}' não encontrado.")
