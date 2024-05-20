import pytest
from class_usuario import Usuario
from class_livro import Livro

import pytest

@pytest.fixture
def usuario_padrao():
    return Usuario(0, "Usuário Padrão")

@pytest.fixture 
def livro_padrao():
    return Livro("Título", 0)

def test_usuario_criacao(usuario_padrao):
    usuario = usuario_padrao  # Usar a fixture como um argumento do teste
    assert usuario.get_id() == 0  # Verificar o ID da fixture
    assert usuario.get_nome() == "Usuário Padrão"

def test_livro_criacao(livro_padrao):
    #tentativa de criar um livro com um ID duplicado
    livro = livro_padrao
    assert livro.id == 0
    assert livro.titulo == "Título"
    assert livro.em_estoque


def test_adiciona_livro(usuario_padrao):
    usuario = usuario_padrao  # Usar a fixture como um argumento do teste
    livro = Livro("1984", 102)
    usuario.adiciona_livro(livro)
    assert usuario.verifica_livro(102)

    with pytest.raises(ValueError):
        usuario.adiciona_livro("não é um livro")

def test_remover_livro(usuario_padrao, livro_padrao):
    #verifico se os livros são de fato removidos 
    usuario = usuario_padrao 
    livro = livro_padrao
    usuario.adiciona_livro(livro)
    assert usuario.verifica_livro(0)
    usuario.remover_livro(0)
    assert not usuario.verifica_livro(0)

def test_verifica_livro(usuario_padrao):
    #adiciono livros e verifico se foram adicionados 
    usuario = usuario_padrao
    livro1 = Livro("Livrasso", 104)
    livro2 = Livro("Livro foda", 105)

    usuario.adiciona_livro(livro1)
    usuario.adiciona_livro(livro2)

    assert usuario.verifica_livro(104)
    assert usuario.verifica_livro(105)
    assert not usuario.verifica_livro(106)

def test_verifica_usuario_sem_livro():
    #verifica se a função tem.livro funciona
    usuario = Usuario(5, "Felipe")
    assert not usuario.tem_livro()

def test_verifica_usuario_com_livro():
    #verifica se, ao adicionar livros, o usuario passa a ter um livro 
    usuario = Usuario(6,"Felipe") 
    assert not usuario.tem_livro()

    livro1 = Livro("titulo", 107)
    usuario.adiciona_livro(livro1)
    assert usuario.tem_livro()

    usuario.remover_livro(107) 
    assert not usuario.tem_livro()

def test_verifica_varios_ids_usuario():
    #verifica se é possível criar vários usuarios com id 0 
    usuario1 = Usuario(0,"felipe0")
    usuario2 = Usuario(0,"felipe1")
    usuario3 = Usuario(0,"felipe2")
    usuario4 = Usuario(0,"felipe3")
    assert isinstance(usuario1, Usuario) 
    assert isinstance(usuario2, Usuario)
    assert isinstance(usuario3, Usuario)
    assert isinstance(usuario4, Usuario)

def test_verifica_varios_ids_livro():
    #verifica se é possível criar vários livros com id 0 

    livro1 = Livro("titulo1", 0) 
    livro2 = Livro("titulo2", 0)
    livro3 = Livro("titulo3", 0)
    assert isinstance(livro1, Livro) 
    assert isinstance(livro3, Livro)
    assert isinstance(livro2, Livro)
    
def test_listar_titulos_livros(usuario_padrao):
    usuario = usuario_padrao
    livro1 = Livro("1984", 0)
    livro2 = Livro("Brave New World",0)
    usuario.adiciona_livro(livro1)
    usuario.adiciona_livro(livro2)
    
    titulos = usuario.listar_titulos_livros()
    assert "1984" in titulos
    assert "Brave New World" in titulos
    assert len(titulos) == 2

def test_listar_ids_livros(usuario_padrao):
    usuario = usuario_padrao
    livro1 = Livro("1984", 33)
    livro2 = Livro("Brave New World",333)
    usuario.adiciona_livro(livro1)
    usuario.adiciona_livro(livro2)
    
    ids = usuario.listar_ids_livros()
    assert 33 in ids
    assert 333 in ids
    assert len(ids) == 2

if __name__ == "__main__":
    pytest.main()
