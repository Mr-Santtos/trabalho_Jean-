def anexar_conteudo(nome_arquivo, conteudo_extra):
    with open(nome_arquivo, 'a', encoding='utf-8') as f:
        f.write(conteudo_extra)
