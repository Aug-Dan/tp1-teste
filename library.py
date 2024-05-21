from book import Book
from user import User

class Library:
    def __init__(self):
        self.users = {}
        self.books = {}

    def adicionar_usuario(self, usuario):
        if usuario.CPF in self.users:
            raise ValueError("Usuário com este CPF já existe.")
        self.users[usuario.CPF] = usuario

    def remover_usuario(self, cpf):
        if cpf in self.users:
            del self.users[cpf]
        else:
            raise ValueError("Usuário não encontrado.")

    def adicionar_livro(self, livro):
        if livro.id in self.books:
            raise ValueError("Livro com este ID já existe.")
        self.books[livro.id] = livro

    def remover_livro(self, livro_id):
        if livro_id in self.books:
            del self.books[livro_id]
        else:
            raise ValueError("Livro não encontrado.")

    def emprestar_livro(self, cpf, livro_id):
        if cpf not in self.users:
            raise ValueError("Usuário não encontrado.")
        if livro_id not in self.books:
            raise ValueError("Livro não encontrado.")
        livro = self.books[livro_id]
        usuario = self.users[cpf]
        if not livro.borrowed:
            usuario.add_book(livro)
            livro.borrowed = True
        else:
            raise ValueError("Livro não está disponível para empréstimo.")

    def devolver_livro(self, cpf, livro_id):
        if cpf not in self.users:
            raise ValueError("Usuário não encontrado.")
        usuario = self.users[cpf]
        if usuario.remove_book(livro_id):
            self.books[livro_id].borrowed = False
        else:
            raise ValueError("Usuário não possui este livro.")

    def consultar_livro(self, termo):
        if isinstance(termo, int):
            return self.books.get(termo).title if termo in self.books else None
        elif isinstance(termo, str):
            ids = [livro_id for livro_id, livro in self.books.items() if livro.title == termo]
            return ids if ids else None
        else:
            raise ValueError("Termo de consulta inválido. Use um ID (int) ou um título (str).")