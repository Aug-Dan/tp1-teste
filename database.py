
import sqlite3

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

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (

)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS loans (
    user INTEGER NOT NULL,
    book_id INTEGER PRIMARY KEY,
    
    
)
''')