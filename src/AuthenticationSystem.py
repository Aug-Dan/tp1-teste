from User import User
from enum import Enum

PASSWORD_COLUMN = 3  # coluna da senha no banco de dados
IS_ADMIN_COLUMN = 4  # coluna is_admin no banco de dados
MAX_ATTEMPTS = 5

class UserType(Enum):
    Student = 0
    Admin = 1

FAILED_TO_LOGIN = -1

class AuthenticationSystem:
    def __init__(self, cursor):
        self.cursor = cursor
    
    def login(self):
        try:
            cpf = int(input("Digite o CPF: "))
            self.cursor.execute("SELECT * FROM users WHERE cpf = ?", (cpf,))
            result = self.cursor.fetchone()
            if result is None:
                return "Usuário não encontrado"
            else:
                user = User(*result)  # Constrói um objeto User a partir dos resultados
                attempts = 0
                while attempts < MAX_ATTEMPTS:
                    password = input("Digite a senha: ")
                    if password == user.get_password():
                        print("Logado com sucesso")
                        return UserType.Admin if user.get_is_admin() else UserType.Student
                    else:
                        attempts += 1
                        print(f"Senha incorreta. Tente novamente. Tentativas Restantes = {MAX_ATTEMPTS - attempts}")
                print("Número máximo de tentativas atingido")
                return FAILED_TO_LOGIN
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return FAILED_TO_LOGIN

    def register(self):
        try:
            cpf = int(input("Digite o CPF: "))
            self.cursor.execute("SELECT * FROM users WHERE cpf = ?", (cpf,))
            result = self.cursor.fetchone()
            if result is not None:
                return "Usuário já existe"
            else:
                name = input("Digite o nome: ")
                password = input("Digite a senha: ")
                is_admin = input("É admin? (s/n): ").lower() == 's'
                self.cursor.execute("INSERT INTO users (cpf, name, password, is_admin) VALUES (?, ?, ?, ?)",
                                    (cpf, name, password, is_admin))
                return "Usuário registrado com sucesso"
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return "Erro ao registrar usuário"
