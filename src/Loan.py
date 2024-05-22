from datetime import datetime, timedelta
from Book import Book
from User import User
import holidays

MAX_RENEWALS = 3
LOAN_PERIOD_DAYS = 14

class Loan:

    def __init__(self, db_manager, user, book, loan_date):
        if not isinstance(loan_date, datetime):
            raise TypeError("loan_date deve ser do tipo datetime")
        self.db_manager = db_manager
        self.user = user
        self.book = book
        self.loan_date = loan_date
        self.due_date = loan_date + timedelta(days=LOAN_PERIOD_DAYS)
        self.renewals = 0
        
    def calculate_due_date(self):
        due_date = self.due_date + timedelta(days=LOAN_PERIOD_DAYS)
        
        # Verifica se a data de vencimento é um fim de semana ou feriado
        while due_date.weekday() >= 5 or due_date in holidays.Brazil():
            due_date += timedelta(days=1)
        
        return due_date

    def renew(self):
        if (self.renewals < MAX_RENEWALS):
            self.due_date = self.calculate_due_date()
            self.renewals += 1
        else:
            raise ValueError("Número máximos de renovações atingido")
    
    def __repr__(self):
        return f"Loan({self.user}, {self.book}, {self.due_date}, {self.renewals} renewals)"            

    
