import pytest
from unittest.mock import MagicMock, call
from src.Library import Library
from src.User import User
from src.Book import Book
from src.Loan import Loan
from datetime import datetime, timedelta 
LOAN_PERIOD_DAYS = 14 


@pytest.fixture
def setup():
    mock_db = MagicMock()
    library = Library(mock_db)
    return library, mock_db

def test_add_user(setup):
    library, mock_db = setup
    user = User(CPF="12345678900", name="Test User", email="test@example.com", password="Password#", is_admin=False)

    library.add_user(user)

    mock_db.execute_query.assert_called_once_with(
        "INSERT INTO users (cpf, name, email, password, is_admin, current_loans_count) VALUES (?, ?, ?, ?, ?, ?)",
        (user.CPF, user.name, user.email, user.password, user.is_admin, user.current_loans_count)
    )
    mock_db.commit.assert_called_once()

def test_add_book(setup):
    library, mock_db = setup
    book = Book(id=1, title="Sample Book", author="Sample Author", genre="Sample Genre")

    library.add_book(book)

    mock_db.execute_query.assert_called_once_with(
        "INSERT INTO books (id, title, author, genre, borrowed) VALUES (?, ?, ?, ?, ?)",
        (book.id, book.title, book.author, book.genre, book.borrowed)
    )
    mock_db.commit.assert_called_once() 

def test_remove_user(setup):
    library, mock_db = setup
    user = User(CPF="12345678900", name="Test User", email="test@example.com", password="Password#", is_admin=False)

    library.add_user(user)
    mock_db.reset_mock()  

    library.remove_user(user.get_CPF())

    mock_db.execute_query.assert_has_calls([
        call("SELECT * FROM users WHERE cpf=?", (user.get_CPF(),)),
        call("DELETE FROM users WHERE cpf=?", (user.get_CPF(),))
    ])
    mock_db.commit.assert_called_once() 

def test_remove_book(setup):
    library, mock_db = setup
    book = Book(id=1, title="Sample Book", author="Sample Author", genre="Sample Genre")

    
    library.add_book(book)
    mock_db.reset_mock()  

    library.remove_book(book.get_id())

    mock_db.execute_query.assert_has_calls([
        call("SELECT * FROM books WHERE id=?", (book.get_id(),)),
        call("DELETE FROM books WHERE id=?", (book.get_id(),))
    ])
    mock_db.commit.assert_called_once() 

def test_loan_book(setup):
    library, mock_db = setup
    user = User(CPF="12345678900", name="Test User", email="test@example.com", password="Password#", is_admin=False)
    book = Book(id=1, title="Sample Book", author="Sample Author", genre="Sample Genre")
    loan_date = datetime.now()

    library.add_user(user)
    library.add_book(book)
    mock_db.reset_mock()  

    loan = Loan(user.CPF, book.id, loan_date)
    library.loan_book(loan)

    mock_db.execute_query.assert_called_once_with(
        "INSERT into loans (user, book_id, loan_date, return_date, renewal_credits) VALUES (?, ?, ?, ?, ?)",
        (loan.user, loan.book, loan.loan_date, loan.due_date, loan.renewals)
    )
    mock_db.commit.assert_called_once()


def test_return_book(setup):
    library, mock_db = setup
    user = User(CPF="12345678900", name="Test User", email="test@example.com", password="Password#", is_admin=False)
    book = Book(id=1, title="Sample Book", author="Sample Author", genre="Sample Genre")
    loan_date = datetime.now()

    library.add_user(user)
    library.add_book(book)

    loan = Loan(user.CPF, book.id, loan_date)
    library.loan_book(loan)
    mock_db.reset_mock()  

    library.return_book(user.CPF, book.id)

    mock_db.execute_query.assert_any_call(
        "DELETE FROM loans WHERE user = ? AND book_id = ?",
        (user.CPF, book.id)
    )
    mock_db.execute_query.assert_any_call(
        "UPDATE books SET borrowed = FALSE WHERE id = ?",
        (book.id,)
    )
    mock_db.commit.assert_called_once()

def test_authenticate_user(setup):
    library, mock_db = setup
    user = User(CPF="12345678900", name="Test User", email="test@example.com", password="Password#", is_admin=False)

    # Adiciona o usuário ao banco de dados
    library.add_user(user)
    mock_db.reset_mock()  # Limpa as chamadas anteriores do mock

    # Simula a resposta do banco de dados para a consulta de autenticação de usuário
    mock_db.execute_query.return_value.fetchone.return_value = (user.CPF, user.name, user.email, user.password, user.is_admin, user.current_loans_count)

    authenticated_user = library.authenticate_user(user.email, user.password)

    assert authenticated_user is not None
    assert authenticated_user.get_email() == user.email
    assert authenticated_user.get_password() == user.password

    mock_db.execute_query.assert_called_once_with(
        "SELECT * FROM users WHERE email = ? AND password = ?",
        (user.email, user.password)
    )
