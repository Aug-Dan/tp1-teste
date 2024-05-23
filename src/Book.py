class Book:
    
    def __init__(self, id, title, author, genre):
        # Verificar se o id já existe no banco
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = False

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_genre(self):
        return self.genre

    def get_borrowed(self):
        return self.borrowed

