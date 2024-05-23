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
    new_user = admin_user.create_user(CPF="11122233344", name="Novo Usuário", email="novo@example.com", password="novouser123", is_admin=False)
    assert new_user.get_nome() == "Novo Usuário"
    assert new_user.get_CPF() == "11122233344"
    assert new_user.get_email() == "novo@example.com"
    assert new_user.get_password() == "novouser123"
    assert not new_user.get_is_admin()

def test_create_user_regular(regular_user):
    # Testa se um usuário não-administrador não pode criar um novo usuário
    with pytest.raises(PermissionError):
        regular_user.create_user(CPF="11122233344", name="Novo Usuário", email="novo@example.com", password="novouser123", is_admin=False)

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
    other_book = Book(id=2, title="Other Book", author="Other Author", genre="Other Genre")
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

def test_barricade_user_cpf_invalid(admin_user):
    variavel_cpf_admin_user = admin_user.get_CPF()
    assert Barricade.is_valid_cpf(variavel_cpf_admin_user) == False

def test_barricade_user_cpf_valid():
    usuario_comum = User( CPF= 94251657691, name="Admin", email="admin@example.com", password="admin123", is_admin=True)
    assert Barricade.is_valid_cpf(usuario_comum.get_CPF()) == True

def test_barricade_cpf_string():
    x = "14777309665"
    assert Barricade.is_valid_cpf(x) == False
    
def test_barricade_password_valid():
    assert Barricade.is_valid_password("Senha@123") == True 

def test_barricade_password_weak():
    assert Barricade.is_valid_password("Senha1") == False

def test_barricade_password_no_upper():
    assert Barricade.is_valid_password("senha1223@@@") == False 

def test_barricade_password_just_uper():
    assert Barricade.is_valid_password("SENHASECRETAHAAHAHAHAHAHAH@@@@111224") == False 

def test_barricade_password_small():
    assert Barricade.is_valid_password("Se1!") == False 

def test_barricade_password_numer():
    assert Barricade.is_valid_password("12345678910") == False

def test_barricade_is_valid_password_invalid_no_special_char():
    assert Barricade.is_valid_password("Senha1234") == False

def test_barricade_password_with_space():
    assert Barricade.is_valid_password("SENHA com ESP4Ç0") == False

def test_barricade_is_strinf():
    assert Barricade.is_string("string_comum") == True
    assert Barricade.is_string(10) == False 

def test_barricade_is_integer():
    assert Barricade.is_integer(10) == True
    assert Barricade.is_integer(10.4) == False
    assert Barricade.is_integer("teste") == False
    
def test_email_is_valid():

    assert Barricade.is_valid_email("email@gmail.com") 

def test_email_with_numbers():

    assert Barricade.is_valid_email("e22344322@gmail.com")

def test_email_without_at():

    assert not Barricade.is_valid_email("email.com") 

def test_email_without_dot_com():

    assert not Barricade.is_valid_email("email@aaaa")

def test_get_email_of_user(admin_user):

    assert Barricade.is_valid_email(admin_user.get_email())
    
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
    
