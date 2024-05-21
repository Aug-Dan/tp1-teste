import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()