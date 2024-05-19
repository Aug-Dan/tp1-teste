class Livro:
    def __init__(self, nome, id, em_estoque=True):
        self.nome = nome
        self.id = id
        self.em_estoque = em_estoque

class Usuario:
    _ids_existentes = set()

    def __init__(self, id, nome=""):
        if id in Usuario._ids_existentes:
            raise ValueError("ID já existe. Por favor, use um ID único.")
        self.id = id
        self.nome = nome
        self.livros = []
        Usuario._ids_existentes.add(id)

    def get_nome(self):
        return self._nome

    def get_id(self):
        return self._id
    
    def adiciona_livro(self, livro):
        
        if isinstance(livro, Livro):
            self.livros.append(livro)
        else:
            raise ValueError("O objeto adicionado deve ser uma instância da classe Livro.")

    def remover_livro(self, livro_id):
        
        for livro in self.livros:
            if livro.id == livro_id:
                self.livros.remove(livro)
                return True
        return False

    def verifica_livro(self, livro_id):
        
        for livro in self.livros:
            if livro.id == livro_id:
                return True
        return False