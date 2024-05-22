class Book:
    
    def __init__(self, db_manager, id, title, author, genre):
        # Verificar se o id já existe no banco
        self.db_manager = db_manager
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.borrowed = False

    def register_new_book(self, cursor):
        cursor.execute('''
        INSERT INTO books (id, title, author, genre, borrowed) VALUES (?, ?, ?, ?, ?)''', 
        (self.id, self.title, self.author, self.genre, self.borrowed))

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

