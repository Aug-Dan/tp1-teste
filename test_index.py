import pytest
from book import Book
from user import User 
from library import Library
import pytest

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

if __name__ == "__main__":
    pytest.main()
