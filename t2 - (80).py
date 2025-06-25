def escrever_novo_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)
