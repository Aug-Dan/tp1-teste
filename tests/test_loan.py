import pytest
from datetime import datetime, timedelta
from src.Book import Book
from src.User import User
from src.Library import Library
from src.Barricade import Barricade
from src.Loan import Loan, MAX_RENEWALS, LOAN_PERIOD_DAYS
import holidays

# Módulo de feriados do Brasil
br_holidays = holidays.Brazil()

@pytest.fixture
def regular_user():
    # Simulando um usuário não-administrador
    return User(CPF="98765432100", name="Regular", email="regular@example.com", password="regular123", is_admin=False)

@pytest.fixture
def sample_book():
    return Book(id=1, title="Sample Book", author="Sample Author", genre="Sample Genre")

def test_loan_initialization(regular_user,sample_book):
    loan_date = datetime(2023, 5, 20)
    
    loan = Loan(regular_user, sample_book, loan_date)
    
    assert loan.user == regular_user
    assert loan.book == sample_book
    assert loan.loan_date == loan_date
    assert loan.due_date == loan_date + timedelta(days=LOAN_PERIOD_DAYS)
    assert loan.renewals == 0

def test_calculate_due_date(regular_user,sample_book):
    loan_date = datetime(2023, 5, 20)
    
    loan = Loan(regular_user, sample_book, loan_date)
    calculated_due_date = loan.calculate_due_date()
    
    expected_due_date = loan.due_date + timedelta(days=LOAN_PERIOD_DAYS)
    while expected_due_date.weekday() >= 5 or expected_due_date in br_holidays:
        expected_due_date += timedelta(days=1)
    
    assert calculated_due_date == expected_due_date

def test_renew(regular_user,sample_book):
    loan_date = datetime(2023, 5, 20)
    
    loan = Loan(regular_user, sample_book, loan_date)
    
    for _ in range(MAX_RENEWALS):
        old_due_date = loan.due_date
        loan.renew()
        assert loan.due_date > old_due_date
        assert loan.renewals <= MAX_RENEWALS
    
    with pytest.raises(ValueError, match="Número máximos de renovações atingido"):
        loan.renew()

def test_repr(regular_user,sample_book):
    loan_date = datetime(2023, 5, 20)
    
    loan = Loan(regular_user, sample_book, loan_date)
    expected_repr = f"Loan({regular_user}, {sample_book}, {loan.due_date}, {loan.renewals} renewals)"
    
    assert repr(loan) == expected_repr
    
def test_renewal_date_on_holiday(regular_user, sample_book):
    # Coloca o dia de emprestimo 28 dias antes do Natal
    loan_date = datetime(2023, 12, 4)
    
    # Quando cria o empréstimo, a data de vencimento cai para os próximos 14 dias úteis
    loan = Loan(regular_user, sample_book, loan_date)
    
    # Quando for renovar, vai cair no natal
    loan.renew()

    assert loan.due_date not in br_holidays

    assert loan.due_date == datetime(2024, 1, 2)
    
