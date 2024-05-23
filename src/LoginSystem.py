from .User import User
from enum import Enum

PASSWORD_COLLUM = 3 # coluna da senha no banco de dados
MAX_ATTEMPTS = 5


class UserType(Enum):
    Student = 0
    Admin = 1

FAILED_TO_LOGIN = -1

class UserSystem:
    def __init__(self, cursor):
        self.cursor = cursor

    def login(self):
        cpf = int(input("Digite o CPF: "))
        self.cursor.execute("SELECT * FROM users WHERE cpf = ?", (cpf,))
        user : User = self.cursor.fetchone()
        if (user is None):
            return "Usuário não encontrado"
        else:
            attempts = 0
            while attempts < MAX_ATTEMPTS:  # give the user 5 attempts
                password = input("Digite a senha: ")  # get the password from the user
                stored_password = user[PASSWORD_COLLUM]
                if password == stored_password:
                    print("Logado com sucesso")
                    return UserType.Student if user.get_is_admin() else UserType.Admin
                else:
                    print(f"Senha incorreta. Tente novamente. Tentativas Restantes = {attempts}")
            print("Número máximo de tentativas atingido")
            return FAILED_TO_LOGIN

    def register(self):
        cpf = int(input("Digite o CPF: "))
        self.cursor.execute("SELECT * FROM users WHERE cpf = ?", (cpf,))
        user = self.cursor.fetchone()
        if user is not None:
            return "Usuário já existe"
        else:
            name = input("Digite o nome: ")
            password = input("Digite a senha: ")
            is_admin = input("É admin? (s/n): ").lower() == 's'
            self.cursor.execute("INSERT INTO users (cpf, name, password, is_admin) VALUES (?, ?, ?, ?)",
                                (cpf, name, password, is_admin))
            print("Usuário registrado com sucesso")
            return UserType.Admin if is_admin else UserType.Student
    