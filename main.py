import sqlite3
from book import Book
# from class_usuario import Usuario 

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL,
    borrowed BOOLEAN NOT NULL
)
''')

livro1 = Book(10, 'O Hobbit', 'J. R. R. Tolkien', 'Fantasia')
livro1.register_new_book(cursor)

# Commit para salvar 
conn.commit()

# Executar a consulta SQL para selecionar todos os itens na tabela 'livros'
rows = cursor.execute('SELECT * FROM books')

for row in rows:
    print(row)

cursor.close()
conn.close()
