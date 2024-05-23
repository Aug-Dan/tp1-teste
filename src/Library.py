from .Book import Book
from .User import User


class Library:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_user(self, user):
        query = "INSERT INTO users (cpf, name, email, password, is_admin, current_loans_count) VALUES (?, ?, ?, ?, ?, ?)"
        self.db_manager.execute_query(query, (user.CPF, user.name, user.email, user.password, user.is_admin, user.current_loans_count))
        self.db_manager.commit()

    def get_db_manager(self):
        return self.db_manager

    # def remover_usuario(self, cpf):
    #     if cpf in self.users:
    #         del self.users[cpf]
    #     else:
    #         raise ValueError("Usuário não encontrado.")

    # def adicionar_livro(self, livro):
    #     if livro.id in self.books:
    #         raise ValueError("Livro com este ID já existe.")
    #     self.books[livro.id] = livro

    # def remover_livro(self, livro_id):
    #     if livro_id in self.books:
    #         del self.books[livro_id]
    #     else:
    #         raise ValueError("Livro não encontrado.")

    # def emprestar_livro(self, cpf, livro_id):
    #     if cpf not in self.users:
    #         raise ValueError("Usuário não encontrado.")
    #     if livro_id not in self.books:
    #         raise ValueError("Livro não encontrado.")
    #     livro = self.books[livro_id]
    #     usuario = self.users[cpf]
    #     if not livro.borrowed:
    #         usuario.add_book(livro)
    #         livro.borrowed = True
    #     else:
    #         raise ValueError("Livro não está disponível para empréstimo.")

    # def devolver_livro(self, cpf, livro_id):
    #     if cpf not in self.users:
    #         raise ValueError("Usuário não encontrado.")
    #     usuario = self.users[cpf]
    #     if usuario.remove_book(livro_id):
    #         self.books[livro_id].borrowed = False
    #     else:
    #         raise ValueError("Usuário não possui este livro.")

    # def consultar_livro(self, termo):
    #     if isinstance(termo, int):
    #         return self.books.get(termo).title if termo in self.books else None
    #     elif isinstance(termo, str):
    #         ids = [livro_id for livro_id, livro in self.books.items() if livro.title == termo]
    #         return ids if ids else None
    #     else:
    #         raise ValueError("Termo de consulta inválido. Use um ID (int) ou um título (str).")