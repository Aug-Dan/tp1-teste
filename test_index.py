import pytest
from index import Livro, Usuario

def test_usuario_criacao():
    #tentativa de criar um usuário com um ID duplicado
    usuario = Usuario(1, "João")
    assert usuario.get_id() == 1
    assert usuario.get_nome() == "João"

    with pytest.raises(ValueError):
        Usuario(1, "Maria")  

def test_livro_criacao():
    #tentativa de criar um livro com um ID duplicado
    livro = Livro("1984", 101)
    assert livro.id == 101
    assert livro.nome == "1984"
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

    livro1 = Livro("titulo", 111)
    usuario.adiciona_livro(livro1)
    assert usuario.tem_livro()

    usuario.remover_livro(111) 
    assert not usuario.tem_livro()


if __name__ == "__main__":
    pytest.main()
