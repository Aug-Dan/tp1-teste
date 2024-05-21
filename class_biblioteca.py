from book import Livro 
from class_usuario import Usuario 

class Biblioteca:
    def __init__(self):
        self.usuarios = {}
        self.livros = {}

    def adicionar_usuario(self, usuario):
        if usuario.id in self.usuarios:
            raise ValueError("Usuário com este ID já existe.")
        self.usuarios[usuario.id] = usuario

    def remover_usuario(self, usuario_id):
        if usuario_id in self.usuarios:
            del self.usuarios[usuario_id]
        else:
            raise ValueError("Usuário não encontrado.")

    def adicionar_livro(self, livro):
        if livro.id in self.livros:
            raise ValueError("Livro com este ID já existe.")
        self.livros[livro.id] = livro

    def remover_livro(self, livro_id):
        if livro_id in self.livros:
            del self.livros[livro_id]
        else:
            raise ValueError("Livro não encontrado.")

    def emprestar_livro(self, usuario_id, livro_id):
        if usuario_id not in self.usuarios:
            raise ValueError("Usuário não encontrado.")
        if livro_id not in self.livros:
            raise ValueError("Livro não encontrado.")
        livro = self.livros[livro_id]
        usuario = self.usuarios[usuario_id]
        if livro.em_estoque:
            usuario.adiciona_livro(livro)
            livro.em_estoque = False
        else:
            raise ValueError("Livro não está em estoque.")

    def devolver_livro(self, usuario_id, livro_id):
        if usuario_id not in self.usuarios:
            raise ValueError("Usuário não encontrado.")
        usuario = self.usuarios[usuario_id]
        if usuario.remover_livro(livro_id):
            self.livros[livro_id].em_estoque = True
        else:
            raise ValueError("Usuário não possui este livro.")
        
   # def consultar_livro_titulo(self, livro_titulo):
    #    if livro_titulo not in self.livros:
     #       raise ValueError("Livro não encontrado.")
      #  return self.livros

    def consultar_livro(self, termo):
        if isinstance(termo, int):
            return self.livros.get(termo).titulo if termo in self.livros else None
        elif isinstance(termo, str):
            ids = [livro_id for livro_id, livro in self.livros.items() if livro.titulo == termo]
            return ids if ids else None
        else:
            raise ValueError("Termo de consulta inválido. Use um ID (int) ou um título (str).")
