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
    
    def create_user(self, CPF, name, email, password, is_admin):
        if self.is_admin:
            return User(CPF, name, email, password, is_admin)
        else:
            raise PermissionError("Apenas administradores podem criar novos usuários.")

    def add_book(self, book):
        self.loans.append(book)
        self.current_loans_count += 1

    def remove_book(self, book_id):
        for book in self.loans:
            if book.id == book_id:
                self.loans.remove(book)
                self.current_loans_count -= 1
                return True
        return False


    def has_books(self):
        return self.current_loans_count > 0    
    