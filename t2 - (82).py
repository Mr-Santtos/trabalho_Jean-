def somar_numeros_arquivo(nome_arquivo):
    total = 0
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                try:
                    total += int(linha.strip())
                except ValueError:
                    pass  
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return 0
    return total
