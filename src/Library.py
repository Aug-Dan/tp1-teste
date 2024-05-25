from src.Book import Book
from src.User import User
from src.Loan import Loan
from src.DatabaseManager import DatabaseManager
from datetime import timedelta


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
    
    def return_book(self, cpf, book_id):
        # Remove o empréstimo da tabela loans
        self.db_manager.execute_query("DELETE FROM loans WHERE user = ? AND book_id = ?", (cpf, book_id))
        
        # Atualiza o status do livro na tabela books
        self.db_manager.execute_query("UPDATE books SET borrowed = FALSE WHERE id = ?", (book_id,))
        
        # Commit das alterações no banco de dados
        self.db_manager.commit()

    def renew_book(self, book_id):
        # Consulta para verificar o empréstimo do livro e obter os valores de return_date e renewal_credits
        loan = self.db_manager.execute_query(
            "SELECT return_date, renewal_credits FROM loans WHERE book_id = ?",
            (book_id,)
        ).fetchone()
        
        if loan is None:
            raise ValueError("Empréstimo não encontrado para o livro especificado.")
        
        return_date, renewal_credits = loan
        
        # Verifica se o empréstimo tem créditos de renovação
        if renewal_credits > 0:
            new_return_date = return_date + timedelta(weeks=1)
            new_renewal_credits = renewal_credits - 1
            
            # Atualiza a tabela loans com a nova data de devolução e créditos de renovação
            self.db_manager.execute_query(
                "UPDATE loans SET return_date = ?, renewal_credits = ? WHERE book_id = ?",
                (new_return_date, new_renewal_credits, book_id)
            )
            
            # Commit das alterações no banco de dados
            self.db_manager.commit()
        else:
            raise ValueError("Renovações esgotadas.")

    def get_db_manager(self):
        return self.db_manager
    
    def show_collection(self):
        self.db_manager.execute_query("SELECT * FROM books")
        books = self.db_manager.fetchall()
        
        if not books:
            print("Ainda não existem livros no banco de dados")
        else:
            for book in books:
                print(book)  # Use print em vez de book.__repr__()

