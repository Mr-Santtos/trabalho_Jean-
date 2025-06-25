class DigitoDisplay:
    representacoes = {
        '0': [
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        '1': [
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 1]
        ],
        '2': [
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1]
        ],
        '3': [
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1]
        ],
        '4': [
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 0, 1],
            [0, 0, 1]
        ],
        '5': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1]
        ],
        '6': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        '7': [
            [1, 1, 1],
            [0, 0, 1],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ],
        '8': [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ],
        '9': [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 0, 1],
            [1, 1, 1]
        ],
        'A': [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1]
        ],
        'B': [  
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 0]
        ],
        'C': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 1]
        ],
        'D': [
            [1, 1, 0],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 0]
        ],
        'E': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1]
        ],
        'F': [
            [1, 1, 1],
            [1, 0, 0],
            [1, 1, 1],
            [1, 0, 0],
            [1, 0, 0]
        ]
    }

    def __init__(self, valor_decimal):
        if valor_decimal < 10:
            self.caractere = str(valor_decimal)
        else:
            self.caractere = chr(ord('A') + valor_decimal - 10)
        self.valor_decimal = valor_decimal
        self.representacao_binaria = DigitoDisplay.representacoes[self.caractere]

    def obter_representacao_binaria(self):
        return self.representacao_binaria


class DisplayDigital:
    def __init__(self, num_digitos):
        self.num_digitos = num_digitos
        self.largura_digito = 3
        self.altura_digito = 5
        self.digitos = [DigitoDisplay(0) for _ in range(num_digitos)]

    def exibir_numero(self, numero_str, base):
        numero_str = numero_str.upper()
        valid_chars = "0123456789ABCDEF"[:base]

        for c in numero_str:
            if c not in valid_chars:
                print(f"Erro: Dígito '{c}' inválido para base {base}")
                return

        if len(numero_str) > self.num_digitos:
            print("Número muito grande para o display")
            return


        num_zeros = self.num_digitos - len(numero_str)
        completo = '0' * num_zeros + numero_str

        self.digitos = []
        for c in completo:
            if c.isdigit():
                val = int(c)
            else:
                val = ord(c) - ord('A') + 10
            self.digitos.append(DigitoDisplay(val))

    def renderizar_display(self):
        largura_total = self.num_digitos * self.largura_digito + (self.num_digitos - 1)
        altura = self.altura_digito
        matriz_display = [[0] * largura_total for _ in range(altura)]

        for i, digito in enumerate(self.digitos):
            matriz_digito = digito.obter_representacao_binaria()
            coluna_inicio = i * (self.largura_digito + 1)
            for linha in range(altura):
                for col in range(self.largura_digito):
                    matriz_display[linha][coluna_inicio + col] = matriz_digito[linha][col]

        for linha in matriz_display:
            linha_str = ''.join('*' if x == 1 else ' ' for x in linha)
            print(linha_str)


if __name__ == "__main__":
    display = DisplayDigital(num_digitos=2)

    print("Simulador de Display Digital")
    while True:
        num = input("Digite um número (ou 'sair' para encerrar): ").strip()
        if num.lower() == 'sair':
            break
        base = input("Digite a base do número (2 a 16): ").strip()
        if not base.isdigit() or not (2 <= int(base) <= 16):
            print("Base inválida! Tente novamente.")
            continue
        base = int(base)

        display.exibir_numero(num, base)
        display.renderizar_display()
        print()
