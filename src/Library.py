from Book import Book
from User import User

class Library:
    def __init__(self):
        self.users = {}
        self.books = {}

    def add_user(self, usuario):
        if usuario.CPF in self.users:
            raise ValueError("Usuário com este CPF já existe.")
        self.users[usuario.CPF] = usuario

    def delete_user(self, cpf):
        if cpf in self.users:
            del self.users[cpf]
        else:
            raise ValueError("Usuário não encontrado.")

    def add_book(self, livro):
        if livro.id in self.books:
            raise ValueError("Livro com este ID já existe.")
        self.books[livro.id] = livro

    def delete_book(self, livro_id):
        if livro_id in self.books:
            del self.books[livro_id]
        else:
            raise ValueError("Livro não encontrado.")

    def lend_book(self, cpf, livro_id):
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

    def return_book(self, cpf, livro_id):
        if cpf not in self.users:
            raise ValueError("Usuário não encontrado.")
        usuario = self.users[cpf]
        if usuario.remove_book(livro_id):
            self.books[livro_id].borrowed = False
        else:
            raise ValueError("Usuário não possui este livro.")

    def query_book(self, termo):
        if isinstance(termo, int):
            return self.books.get(termo).title if termo in self.books else None
        elif isinstance(termo, str):
            ids = [livro_id for livro_id, livro in self.books.items() if livro.title == termo]
            return ids if ids else None
        else:
            raise ValueError("Termo de consulta inválido. Use um ID (int) ou um título (str).")