class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def detalhes(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}")
