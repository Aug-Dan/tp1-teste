import pytest
from src.Book import Book
from src.User import User
from srd.Libray import Library

def test_get_nome():
    user = User("12345678900", "Test User", "test@example.com", "password", False)
    assert user.get_nome() == "Test User"

def test_get_CPF():
    user = User("12345678900", "Test User", "test@example.com", "password", False)
    assert user.get_CPF() == "12345678900"

def test_get_email():
    user = User("12345678900", "Test User", "test@example.com", "password", False)
    assert user.get_email() == "test@example.com"

def test_get_password():
    user = User("12345678900", "Test User", "test@example.com", "password", False)
    assert user.get_password() == "password"

def test_get_is_admin():
    user = User("12345678900", "Test User", "test@example.com", "password", False)
    assert user.get_is_admin() == False

def test_create_user():
    user = User("12345678900", "Test User", "test@example.com", "password", False)
    assert user.get_nome() == "Test User"
    assert user.get_CPF() == "12345678900"
    assert user.get_email() == "test@example.com"
    assert user.get_password() == "password"
    assert not user.get_is_admin()

def test_create_admin_user():
    admin = User("12345678901", "Admin User", "admin@example.com", "password", True)
    new_user = admin.create_user("98765432100", "New User", "new@example.com", "password", False)
    assert new_user.get_nome() == "New User"
    assert new_user.get_CPF() == "98765432100"

def test_create_user_without_permission():
    user = User("12345678900", "Test User", "test@example.com", "password", False)
    with pytest.raises(PermissionError):
        user.create_user("98765432100", "New User", "new@example.com", "password", False)


def test_create_book():
    book = Book(1, "Test Book", "Author", "Genre")
    assert book.id == 1
    assert book.title == "Test Book"
    assert book.author == "Author"
    assert book.genre == "Genre"
    assert not book.borrowed

def test_library_adicionar_usuario():
    library = Library()
    user = User("12345678900", "Test User", "test@example.com", "password", False)
    library.adicionar_usuario(user)
    assert library.users["12345678900"] == user

def test_library_remover_usuario():
    library = Library()
    user = User("12345678900", "Test User", "test@example.com", "password", False)
    library.adicionar_usuario(user)
    library.remover_usuario("12345678900")
    assert "12345678900" not in library.users

def test_library_adicionar_livro():
    library = Library()
    book = Book(1, "Test Book", "Author", "Genre")
    library.adicionar_livro(book)
    assert library.books[1] == book

def test_library_remover_livro():
    library = Library()
    book = Book(1, "Test Book", "Author", "Genre")
    library.adicionar_livro(book)
    library.remover_livro(1)
    assert 1 not in library.books


def test_library_consultar_livro_por_id():
    library = Library()
    book = Book(1, "Test Book", "Author", "Genre")
    library.adicionar_livro(book)
    assert library.consultar_livro(1) == "Test Book"

def test_library_consultar_livro_por_titulo():
    library = Library()
    book1 = Book(1, "Test Book", "Author", "Genre")
    book2 = Book(2, "Test Book", "Author", "Genre")
    library.adicionar_livro(book1)
    library.adicionar_livro(book2)
    assert library.consultar_livro("Test Book") == [1, 2]
