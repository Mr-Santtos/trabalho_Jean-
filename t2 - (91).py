class Livro:
    total_livros = 0

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Livro.total_livros += 1

    def detalhes(self):
        print(f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}")

    @classmethod
    def mostrar_total_livros(cls):
        print(f"Total de livros criados: {cls.total_livros}")
