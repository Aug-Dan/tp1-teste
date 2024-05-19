import pytest
from index import Livro, Usuario

def test_usuario_criacao():
    usuario = Usuario(1, "João")
    assert usuario.get_id() == 1
    assert usuario.get_nome() == "João"

    with pytest.raises(ValueError):
        Usuario(1, "Maria")  # Tentativa de criar um usuário com um ID duplicado

def test_livro_criacao():
    livro = Livro("1984", 101)
    assert livro.id == 101
    assert livro.nome == "1984"
    assert livro.em_estoque

    with pytest.raises(ValueError):
        Livro("Brave New World", 101)  # Tentativa de criar um livro com um ID duplicado

def test_adiciona_livro():
    usuario = Usuario(2, "Maria")
    livro = Livro("1984", 102)

    usuario.adiciona_livro(livro)
    assert usuario.verifica_livro(102)

    with pytest.raises(ValueError):
        usuario.adiciona_livro("não é um livro")

def test_remover_livro():
    usuario = Usuario(3, "Carlos")
    livro = Livro("1984", 103)
    usuario.adiciona_livro(livro)

    assert usuario.verifica_livro(103)
    usuario.remover_livro(103)
    assert not usuario.verifica_livro(103)

def test_verifica_livro():
    usuario = Usuario(4, "Ana")
    livro1 = Livro("1984", 104)
    livro2 = Livro("Brave New World", 105)

    usuario.adiciona_livro(livro1)
    usuario.adiciona_livro(livro2)

    assert usuario.verifica_livro(104)
    assert usuario.verifica_livro(105)
    assert not usuario.verifica_livro(106)

if __name__ == "__main__":
    pytest.main()
