from .Book import Book
from .User import User
from .Loan import Loan


class Library:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_user(self, user):
        query = "INSERT INTO users (cpf, name, email, password, is_admin, current_loans_count) VALUES (?, ?, ?, ?, ?, ?)"
        self.db_manager.execute_query(query, (user.CPF, user.name, user.email, user.password, user.is_admin, user.current_loans_count))
        self.db_manager.commit()

    def remove_user(self, cpf):
        self.db_manager.execute_query("SELECT * FROM users WHERE cpf=?", (cpf,))
        user_to_be_removed = self.db_manager.fetchone()
        if user_to_be_removed is None:
            raise ValueError("Usuário não encontrado.")
        
        self.db_manager.execute_query("DELETE FROM users WHERE cpf=?", (cpf,))
        self.db_manager.commit()

    def add_book(self, book):
        query = "INSERT INTO books (id, title, author, genre, borrowed) VALUES (?, ?, ?, ?, ?)"
        self.db_manager.execute_query(query, (book.id, book.title, book.author, book.genre, book.borrowed))
        self.db_manager.commit()
    
    def remove_book(self, id):
        self.db_manager.execute_query("SELECT * FROM books WHERE id=?", (id,))
        book_to_be_removed = self.db_manager.fetchone()
        if book_to_be_removed is None:
            raise ValueError("Livro não encontrado.")
        
        self.db_manager.execute_query("DELETE FROM books WHERE id=?", (id,))
        self.db_manager.commit()

    def loan_book(self, loan):
        query = "INSERT into loans (user, book_id, loan_date, return_date, renewal_credits) VALUES (?, ?, ?, ?, ?)"
        self.db_manager.execute_query(query, (loan.user, loan.book, loan.loan_date, loan.due_date, loan.renewals))
        self.db_manager.commit()
    
    # def devolver_livro(self, cpf, livro_id):
    #     if cpf not in self.users:
    #         raise ValueError("Usuário não encontrado.")
    #     usuario = self.users[cpf]
    #     if usuario.remove_book(livro_id):
    #         self.books[livro_id].borrowed = False
    #     else:
    #         raise ValueError("Usuário não possui este livro.")

    # def consultar_livro(self, termo):
    #     if isinstance(termo, int):
    #         return self.books.get(termo).title if termo in self.books else None
    #     elif isinstance(termo, str):
    #         ids = [livro_id for livro_id, livro in self.books.items() if livro.title == termo]
    #         return ids if ids else None
    #     else:
    #         raise ValueError("Termo de consulta inválido. Use um ID (int) ou um título (str).") 
    
    def get_db_manager(self):
        return self.db_manager