from User import User

PASSWORD_COLLUM = 3
MAX_ATTEMPTS = 5

class LoginSystem:
    def __init__(self, ):
        return None

    
    def login(self, cursor):
        cpf = int(input("Digite o CPF: "))
        cursor.execute("SELECT * FROM users WHERE cpf = ?", (cpf,))
        user = cursor.fetchone()
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

    