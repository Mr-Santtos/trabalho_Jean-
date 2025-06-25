class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def get_nome(self):
        return self._nome

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def get_idade(self):
        return self._idade

    def set_idade(self, nova_idade):
        self._idade = nova_idade
