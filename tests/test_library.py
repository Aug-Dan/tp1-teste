import pytest
import unittest
from unittest.mock import MagicMock
from unittest.mock import call
from datetime import datetime, timedelta

from src.Library import Library
from src.User import User
from src.Book import Book
from src.Loan import Loan

@pytest.fixture
def setUp():
    # Cria um mock para o database manager
    mock_db = MagicMock()
    library = Library(mock_db)
    user = User(CPF="12345678900", name="Test User", email="test@example.com", 
                password="Password#", is_admin=False)
    book = Book(id="10", title="", author="", genre="")
    
    return library, mock_db, user, book

def test_add_user(setUp):
    library, mock_db, user, book = setUp

    library.add_user(user)
        
    # Verifica se o método execute_query foi chamado com a consulta SQL correta e os parâmetros esperados
    mock_db.execute_query.assert_called_once_with(
            "INSERT INTO users (cpf, name, email, password, is_admin, current_loans_count) VALUES (?, ?, ?, ?, ?, ?)",
            (user.CPF, user.name, user.email, user.password, user.is_admin, user.current_loans_count)
        )

    # Verifica se o método commit foi chamado uma vez
    mock_db.commit.assert_called_once()

def test_remove_user(setUp):
    library, mock_db, user, book = setUp
    mock_db.fetchone.return_value = user.get_CPF

    library.remove_user(User.get_CPF)

    mock_db.execute_query.assert_has_calls([
        call("SELECT * FROM users WHERE cpf=?", (User.get_CPF,)),
        call("DELETE FROM users WHERE cpf=?", (User.get_CPF,))
    ])

    mock_db.commit.assert_called_once()

def test_remove_nonexistent_user(setUp):
    library, mock_db, user, book = setUp
    mock_db.fetchone.return_value = None

    with pytest.raises(ValueError, match="Usuário não encontrado."):
        library.remove_user(User.get_CPF)

def test_add_book(setUp):
    library, mock_db, user, book = setUp
    library.add_book(book)
        
    # Verifica se o método execute_query foi chamado com a consulta SQL correta e os parâmetros esperados
    mock_db.execute_query.assert_called_once_with(
            "INSERT INTO books (id, title, author, genre, borrowed) VALUES (?, ?, ?, ?, ?)",
            (book.id, book.title, book.author, book.genre, book.borrowed))

    # Verifica se o método commit foi chamado uma vez
    mock_db.commit.assert_called_once()

def test_remove_book(setUp):
    library, mock_db, user, book = setUp
    mock_db.fetchone.return_value = book.get_id

    library.remove_book(book.get_id)

    mock_db.execute_query.assert_has_calls([
        call("SELECT * FROM books WHERE id=?", (book.get_id,)),
        call("DELETE FROM books WHERE id=?", (book.get_id,))
    ])

    mock_db.commit.assert_called_once()

def test_remove_nonexistent_book(setUp):
    library, mock_db, user, book = setUp
    mock_db.fetchone.return_value = None

    with pytest.raises(ValueError, match="Livro não encontrado."):
        library.remove_book(book.get_id)

def test_loan_book(setUp):
    library, mock_db, user, book = setUp
    loan_date = datetime.now()

    loan = Loan(user.get_CPF, book.get_id, loan_date)
    library.loan_book(loan)

    # Verifica se o método execute_query foi chamado com a consulta SQL correta e os parâmetros esperados
    mock_db.execute_query.assert_called_once_with(
        "INSERT into loans (user, book_id, loan_date, return_date, renewal_credits) VALUES (?, ?, ?, ?, ?)",
        (loan.user, loan.book, loan.loan_date, loan.due_date, loan.renewals))

    # Verifica se o método commit foi chamado uma vez
    mock_db.commit.assert_called_once()

def test_renew_book_success(setUp):
    library, mock_db, user, book = setUp
    book_id = 1
    return_date = datetime(2024, 5, 24)
    renewal_credits = 1
    # Mock para simular o retorno da consulta SELECT
    mock_db.execute_query.return_value.fetchone.return_value = (return_date, renewal_credits)
        
    library.renew_book(book_id)
        
    # Verifica se a query SELECT foi chamada com os parâmetros corretos
    mock_db.execute_query.assert_any_call(
        "SELECT return_date, renewal_credits FROM loans WHERE book_id = ?",
        (book_id,)
    )
        
    # Verifica se a query UPDATE foi chamada com os parâmetros corretos
    mock_db.execute_query.assert_any_call(
        "UPDATE loans SET return_date = ?, renewal_credits = ? WHERE book_id = ?",
        (return_date + timedelta(weeks=1), renewal_credits - 1, book_id)
    )
        
    # Verifica se o commit foi chamado uma vez
    mock_db.commit.assert_called_once()

def test_renew_book_no_renewals_left(setUp):
    library, mock_db, user, book = setUp
    book_id = 1
    return_date = datetime(2024, 5, 24)
    renewal_credits = 0
        
    # Mock para simular o retorno da consulta SELECT
    mock_db.execute_query.return_value.fetchone.return_value = (return_date, renewal_credits)
        
    with pytest.raises(ValueError, match="Renovações esgotadas."):
        library.renew_book(book_id)
        
    # Verifica se a query SELECT foi chamada com os parâmetros corretos
    mock_db.execute_query.assert_called_with(
        "SELECT return_date, renewal_credits FROM loans WHERE book_id = ?",
        (book_id,)
    )
        
    # Verifica se o commit não foi chamado
    mock_db.commit.assert_not_called()

def test_renew_book_no_loan_found(setUp):
    library, mock_db, user, book = setUp
    book_id = 1
        
    # Mock para simular a ausência de retorno da consulta SELECT
    mock_db.execute_query.return_value.fetchone.return_value = None
        
    with pytest.raises(ValueError, match="Empréstimo não encontrado para o livro especificado."):
        library.renew_book(book_id)
        
    # Verifica se a query SELECT foi chamada com os parâmetros corretos
    mock_db.execute_query.assert_called_with(
        "SELECT return_date, renewal_credits FROM loans WHERE book_id = ?",
        (book_id,)
    )
        
    # Verifica se o commit não foi chamado
    mock_db.commit.assert_not_called()










