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

    def __repr__(self) -> str:
        return (f"Book ID: {self.id}, "
                f"Title: {self.title}, "
                f"Author: {self.author}, "
                f"Genre: {self.genre}, "
                f"Borrowed: {self.borrowed}")

