import sqlite3
from book import Book
from database_manager import DatabaseManager
from user import User
from library import Library

db = DatabaseManager('biblioteca.db')

John = User(db, 70270270270, 'John Marston', 'email@gmail.com', '123', False)

sistema = Library(db)

sistema.add_user(John)

db.commit()

rows = db.execute_query('SELECT * FROM users')

for row in rows:
    print(row)

db.close()
