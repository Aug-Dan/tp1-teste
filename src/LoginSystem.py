from User import User
import sqlite3

PASSWORD_COLLUM = 3
MAX_ATTEMPTS = 5

class LoginSystem:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        self.initialize_database()

    def initialize_database(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
            self._create_tables()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.close()
                
    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cursor = None

    def __del__(self):
        self.close()
        
    def login(self, cpf):
        self.cursor.execute("SELECT * FROM users WHERE cpf = ?", (cpf,))
        user = self.cursor.fetchone()
        if (user is None):
            return "Usuário não encontrado"
        else:
            attempts = 0
            while attempts < MAX_ATTEMPTS:  # give the user 5 attempts
                password = input("Digite a senha: ")  # get the password from the user
                stored_password = user[PASSWORD_COLLUM]
                if password == stored_password:
                    return "Usuário logado com sucesso"
                else:
                    print("Senha incorreta. Tente novamente.")
            return "Número máximo de tentativas atingido"

    