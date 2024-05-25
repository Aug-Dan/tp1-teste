from src.Book import Book
class User:

    def __init__(self, CPF, name, email, password, is_admin):
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
    
    def get_current_loans(self):
        return self.current_loans_count