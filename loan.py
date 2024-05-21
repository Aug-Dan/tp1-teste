from datetime import datetime
from book import Book
from user import User

class Loan:

    def __init__(self, user, book, loan_date, renewal_credits):
        if not isinstance(loan_date, datetime):
            raise TypeError("loan_date deve ser do tipo datetime")

        self.user = user
        self.book = book
        self.loan_date = datetime.now()
        self.return_date = # Calcula uma semana no futuro
        self.renewal_credits = 3

    
