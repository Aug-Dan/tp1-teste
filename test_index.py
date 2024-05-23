import pytest
from src.Book import Book
from src.User import User
from src.Library import Library
from src.Barricade import Barricade

@pytest.fixture
def admin_user():
    # Simulando um usuário administrador
    return User(db_manager=None, CPF="12345678900", name="Admin", email="admin@example.com", password="admin123", is_admin=True)

@pytest.fixture
def regular_user():
    # Simulando um usuário não-administrador
    return User(db_manager=None, CPF="98765432100", name="Regular", email="regular@example.com", password="regular123", is_admin=False)

@pytest.fixture
def sample_book():
    return Book(db_manager=None,id=1, title="Sample Book", author="Sample Author", genre="Sample Genre")

@pytest.fixture
def sample_library():
    # Criando uma instância de biblioteca para teste
    return Library(db_manager=None)

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

def test_create_user_admin(admin_user):
    # Testa se um administrador pode criar um novo usuário
    new_user = admin_user.create_user(db_manager=None,CPF="11122233344", name="Novo Usuário", email="novo@example.com", password="novouser123", is_admin=False)
    assert new_user.get_nome() == "Novo Usuário"
    assert new_user.get_CPF() == "11122233344"
    assert new_user.get_email() == "novo@example.com"
    assert new_user.get_password() == "novouser123"
    assert not new_user.get_is_admin()

def test_create_user_regular(regular_user):
    # Testa se um usuário não-administrador não pode criar um novo usuário
    with pytest.raises(PermissionError):
        regular_user.create_user(db_manager=None,CPF="11122233344", name="Novo Usuário", email="novo@example.com", password="novouser123", is_admin=False)

def test_add_book(admin_user):
    # Testa se a contagem de empréstimos é incrementada corretamente ao adicionar um livro
    initial_count = admin_user.current_loans_count
    admin_user.add_book("Livro 1")
    assert admin_user.current_loans_count == initial_count + 1

def test_get_id(sample_book):
    assert sample_book.get_id() == 1

def test_get_title(sample_book):
    assert sample_book.get_title() == "Sample Book"

def test_get_author(sample_book):
    assert sample_book.get_author() == "Sample Author"

def test_get_genre(sample_book):
    assert sample_book.get_genre() == "Sample Genre"

def test_get_borrowed(sample_book):
    assert sample_book.get_borrowed() == False

def test_get_db_manager(sample_library):
    # Testa se o método get_db_manager retorna o gerenciador de banco de dados corretamente
    assert sample_library.get_db_manager() == None 

def test_user_remove_book(regular_user):
    inicio = regular_user.current_loans_count 
    regular_user.add_book(sample_book)
    regular_user.remove_book(sample_book)
    assert regular_user.current_loans_count == inicio + 0

def test_user_remove_book_zero_count_error(regular_user):
    # Testa se o método remove_book lança um erro ao tentar remover um livro quando a contagem de empréstimos já é zero
    with pytest.raises(ValueError):
        regular_user.remove_book("Sample Book")


def test_user_remove_book_multiple_books(regular_user, sample_book):
    # Testa se o método remove_book decrementa a contagem de empréstimos corretamente quando há múltiplos livros emprestados
    regular_user.add_book(sample_book)  # Adiciona um livro para simular um empréstimo
    regular_user.add_book(sample_book)  # Adiciona outro livro para simular múltiplos empréstimos do mesmo livro
    initial_count = regular_user.current_loans_count
    regular_user.remove_book(sample_book)
    assert regular_user.current_loans_count == initial_count - 1

def test_user_remove_book_different_books(regular_user, sample_book):
    # Testa se o método remove_book decrementa a contagem de empréstimos corretamente quando há diferentes livros emprestados
    other_book = Book(db_manager=None,id=2, title="Other Book", author="Other Author", genre="Other Genre")
    regular_user.add_book(sample_book)  # Adiciona um livro para simular um empréstimo
    regular_user.add_book(other_book)  # Adiciona outro livro para simular um empréstimo diferente
    initial_count = regular_user.current_loans_count
    regular_user.remove_book(sample_book)
    assert regular_user.current_loans_count == initial_count - 1 


def test_barricade_cpf_valid():
    assert Barricade.is_valid_cpf(14777309665) == True 

def test_barricade_cpf_longo():
    assert Barricade.is_valid_cpf(13444588888) == False 

def test_barricade_cpf_curto():
    assert Barricade.is_valid_cpf(1) == False 

def test_barricade_cpf_somente_1():
    assert Barricade.is_valid_cpf(11111111111) == False

def test_barricade_cpf_invalid():
    assert Barricade.is_valid_cpf(12345678900) == False

def test_barricade_is_valid_cpf_zero():
    assert Barricade.is_valid_cpf(00000000000) == False

def test_barricade_user_cpf_valid(admin_user):
    variavel_cpf_admin_user = admin_user.get_CPF()
    assert Barricade.is_valid_cpf(variavel_cpf_admin_user) == False

def test_barricade_cpf_string():
    x = "14777309665"
    assert Barricade.is_valid_cpf(x) == False
    
def test_barricade_password_valid():
    assert Barricade.is_valid_password("Senha@123") == True 

def test_barricade_password_weak():
    assert Barricade.is_valid_password("Senha1") == False

def test_barricade_password_no_upper():
    assert Barricade.is_valid_password("senha1223@@@") == False 