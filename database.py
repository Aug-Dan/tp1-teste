import sqlite3

def create_tables():
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
        cpf INTEGER NOT NULL PRIMARY KEY,
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
        book_id INTEGER,
        loan_date DATE NOT NULL,
        return_date DATE NOT NULL,
        renewal_credits INTEGER CHECK (renewal_credits >= 0 AND renewal_credits <= 3),
        PRIMARY KEY (user, book_id),
        FOREIGN KEY (user) REFERENCES users(cpf),
        FOREIGN KEY (book_id) REFERENCES books(id)
    )
    ''')

    conn.commit()
    cursor.close()
    conn.close()
    
def drop_table(table_name):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    
    conn.commit()
    cursor.close()
    conn.close()

def check_tables():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:", tables)
    
    cursor.close()
    conn.close()

create_tables()
check_tables()

