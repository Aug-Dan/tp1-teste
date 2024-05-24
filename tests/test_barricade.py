import pytest
from src.Barricade import Barricade
from src.User import User
from src.User import User

@pytest.fixture
def admin_user():
    # Simulando um usuário administrador
    return User( CPF="12345678900", name="Admin", email="admin@example.com", password="admin123", is_admin=True)

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

def test_barricade_password_just_upper():
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