from src.User import User
from src.Barricade import Barricade 
from enum import Enum

PASSWORD_COLUMN = 3  # coluna da senha no banco de dados
MAX_ATTEMPTS = 5

class UserType(Enum):
    Student = 0
    Admin = 1

class LoginFailedException(Exception):
    def __init__(self, message="Erro ao fazer login"):
        self.message = message
        super().__init__(self.message)

class AuthenticationSystem:
    def __init__(self, cursor):
        self.cursor = cursor
    
    def login(self):
        try:
            cpf = int(input("Digite o CPF: "))
            self.cursor.execute("SELECT * FROM users WHERE cpf = ?", (cpf,))
            result = self.cursor.fetchone()
            if result is None:
                raise LoginFailedException("Usuário não encontrado")
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
                raise LoginFailedException("Falha ao fazer login: número máximo de tentativas atingido")
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
