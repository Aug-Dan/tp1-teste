import sqlite3
from class_livro import Livro
from class_usuario import Usuario 

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    em_estoque BOOLEAN NOT NULL
)
''')

# # Criar instâncias
# livro1 = Livro('Livro A', 1, True)
# livro2 = Livro('Livro B', 2, False)

# # Salvar os livros no banco de dados
# livro1.salvar_no_banco(cursor)
# livro2.salvar_no_banco(cursor)

# Commit para salvar 
conn.commit()

# Executar a consulta SQL para selecionar todos os itens na tabela 'livros'
rows = cursor.execute('SELECT * FROM livros')

for row in rows:
    print(row)

cursor.close()
conn.close()
