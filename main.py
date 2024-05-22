import sqlite3
from Book import Book
from DatabaseManager import DatabaseManager
from User import User
from Library import Library

db = DatabaseManager('biblioteca.db')

John = User(db, 70270270270, 'John Marston', 'email@gmail.com', '123', False)

sistema = Library(db)

sistema.add_user(John)

db.commit()

rows = db.execute_query('SELECT * FROM users')

for row in rows:
    print(row)

db.close()
