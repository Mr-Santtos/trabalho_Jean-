def ler_csv_simples(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        if not linhas:
            return []
        
        dados = []
        start = 1 if ',' in linhas[0] else 0
        for linha in linhas[start:]:
            linha = linha.strip()
            if linha:
                dados.append(linha.split(','))
        return dados
    except FileNotFoundError:
        print(f"Erro: arquivo '{nome_arquivo}' não encontrado.")
        return []
