import pytest
from src.User import User
from src.Book import Book

@pytest.fixture
def admin_user():
    # Simulando um usuário administrador
    return User( CPF="12345678900", name="Admin", email="admin@example.com", password="admin123", is_admin=True)

@pytest.fixture
def regular_user():
    # Simulando um usuário não-administrador
    return User(CPF="98765432100", name="Regular", email="regular@example.com", password="regular123", is_admin=False)

@pytest.fixture
def sample_book():
    return Book(id=1, title="Sample Book", author="Sample Author", genre="Sample Genre")



def test_get_nome(admin_user):
    # Testa se o método get_nome retorna o nome corretamente
    assert admin_user.get_nome() == "Admin"

def test_get_CPF(admin_user):
    # Testa se o método get_CPF retorna o CPF corretamente
    assert admin_user.get_CPF() == "12345678900"

def test_get_email(admin_user):
    # Testa se o método get_email retorna o email corretamente
    assert admin_user.get_email() == "admin@example.com"

def test_get_password(admin_user):
    # Testa se o método get_password retorna a senha corretamente
    assert admin_user.get_password() == "admin123"

def test_get_is_admin(admin_user):
    # Testa se o método get_is_admin retorna se o usuário é administrador corretamente
    assert admin_user.get_is_admin() == True