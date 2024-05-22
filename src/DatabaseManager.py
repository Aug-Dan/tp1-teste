import sqlite3

DATABASE_PATH = "../biblioteca.db"

class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()

    def initialize_database(self):
        try:
            self.connection = sqlite3.connect(self.DATABASE_PATH)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.close()
                
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def __del__(self):
        self.close()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()