from Book import Book
class User:

    def __init__(self, db_manager, CPF, name, email, password, is_admin):
        self.db_manager = db_manager
        self.CPF = CPF
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.current_loans_count = 0

    def get_nome(self):
        return self.name

    def get_CPF(self):
        return self.CPF

    def get_email(self):
        return self.email 
    
    def get_password(self):
        return self.password 
    
    def get_is_admin(self):
        return self.is_admin
    
    def create_user(self, db_manager, CPF, name, email, password, is_admin):
        if self.is_admin:
            return User(db_manager, CPF, name, email, password, is_admin)
        else:
            raise PermissionError("Apenas administradores podem criar novos usuários.")

    # Métodos de 

    # def add_book(self, book):
    #     self.current_loans_count += 1

    # def remove_book(self, book):
    #     if self.current_loans_count == 0:
    #         raise ValueError("A contagem de empréstimos já é zero. Não é possível remover mais livros.")
    #     self.current_loans_count -= 1