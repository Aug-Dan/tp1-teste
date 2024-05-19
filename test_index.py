import pytest
from class_usuario import Usuario
from class_livro import Livro
"""
@pytest.fixture
def usuario_padrao():
    return Usuario(1001, "Usuário Padrão")
"""

def test_usuario_criacao():

    usuario = Usuario(1, "Usuário Padrão")
    assert usuario.get_id() == 1
    assert usuario.get_nome() == "Usuário Padrão"

    with pytest.raises(ValueError):
        Usuario(1, "Maria")  

def test_livro_criacao():
    #tentativa de criar um livro com um ID duplicado
    livro = Livro("1984", 101)
    assert livro.id == 101
    assert livro.titulo == "1984"
    assert livro.em_estoque

    with pytest.raises(ValueError):
        Livro("Brave New World", 101)  

def test_adiciona_livro():
    #verifica se os livros são adicionados corretamente 
    usuario = Usuario(2, "Maria")
    livro = Livro("1984", 102)

    usuario.adiciona_livro(livro)
    assert usuario.verifica_livro(102)

    with pytest.raises(ValueError):
        usuario.adiciona_livro("não é um livro")

def test_remover_livro():
    #verifico se os livros são de fato removidos 
    usuario = Usuario(3, "Carlos")
    livro = Livro("1984", 103)
    usuario.adiciona_livro(livro)

    assert usuario.verifica_livro(103)
    usuario.remover_livro(103)
    assert not usuario.verifica_livro(103)

def test_verifica_livro():
    #adiciono livros e verifico se foram adicionados 
    usuario = Usuario(4, "Ana")
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
    
if __name__ == "__main__":
    pytest.main()
