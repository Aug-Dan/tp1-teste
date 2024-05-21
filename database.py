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
    CPF INTEGER NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    is_admin BOOLEAN NOT NULL,
    current_loans_count INTEGER CHECK (current_loans_count >= 0 AND current_loans_count <= 3)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS loans (
    user INTEGER NOT NULL,
    book_id INTEGER PRIMARY KEY,
    loan_date DATE NOT NULL,
    return_date DATE NOT NULL,
    renewal_credits INTEGER CHECK (renewal_credits >= 0 AND renewal_credits <= 3)   
)
''')

conn.commit()
cursor.close()
conn.close()