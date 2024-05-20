class Book:
    
    def __init__(self, id, title, author, genre):
        # Verificar se o id já existe no banco
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = False

    def register_new_book(self, cursor):
        cursor.execute('''
        INSERT INTO books (id, title, author, genre, borrowed) VALUES (?, ?, ?, ?, ?)''', 
        (self.id, self.title, self.author, self.genre, self.borrowed))

# class Livro:
#     _ids_existentes = set()

#     def __init__(self, id, titulo, autor, genero, emprestado=True):
#         if id in Livro._ids_existentes and id != 0:
#             raise ValueError("ID já existe. Por favor, use um ID único.")
#         self.id = id
#         self.titulo = titulo
#         self.autor = autor
#         self.genero = genero
#         self.em_estoque = emprestado
#         Livro._ids_existentes.add(id)

#     def salvar_no_banco(self, cursor):
#         cursor.execute('''
#         INSERT INTO livros (id, titulo, autor, genero, em_estoque) VALUES (?, ?, ?, ?, ?)
#         ''', (self.id, self.titulo, self.autor, self.genero, self.em_estoque))
