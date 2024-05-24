import sqlite3

DATABASE_PATH = "../biblioteca.db"

class DatabaseManager:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DatabaseManager, cls).__new__(cls)
            cls.__instance.connection = None
            cls.__instance.cursor = None
        return cls.__instance

    def initialize_database(self):
        if self.connection is None or self.cursor is None:
            try:
                self.connection = sqlite3.connect(DATABASE_PATH)
                self.cursor = self.connection.cursor()
            except sqlite3.Error as e:
                print(f"Erro ao conectar ao banco de dados: {e}")
                self.close()

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor

    def fetchone(self):
        return self.cursor.fetchone()
    
    def commit(self):
        self.connection.commit()
    
    def __del__(self):
        self.close()