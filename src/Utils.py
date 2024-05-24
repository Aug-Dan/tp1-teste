from src.Library import Library
from src.User import User
from src.Loan import Loan, datetime
from src.Book import Book
from src.AuthenticationSystem import AuthenticationSystem, UserType
from src.DatabaseManager import DatabaseManager

from colorama import Fore, Style

class Menu:
    @staticmethod
    def display_welcome():
        keep_going = True
        db_manager = DatabaseManager()
        db_manager.initialize_database()
        library = Library(db_manager) 
        
        print(Fore.GREEN + "Seja Bem Vindo ao Sistema" + Style.RESET_ALL)
        
        while (keep_going):
            print(Fore.BLUE + "1 - Exibir Coleção")
            print("2 - Logar no sistema")
            print("3 - Sair" + Style.RESET_ALL)
            
            option = int(input(Fore.YELLOW + "Digite uma opção (1 - 3): " + Style.RESET_ALL))
            
            match option:
                case 1:
                    library.show_collection()
                    
                case 2: 
                    # Pede para o usuário logar no sistema
                    auth = AuthenticationSystem(db_manager)
                    
                    try:
                        result = auth.login()
                        if (result == UserType.Student):
                            Menu.display_user_menu(library)
                            
                        elif (result == UserType.Admin):
                            Menu.display_admin_menu(library)
                            
                    except Exception as e:
                        print(f"Ocorreu um erro durante o login: {e}")
                        
                case 3:
                    keep_going = False
                    
                case _:
                    print(Fore.RED + "Opção inválida. Por favor, tente novamente." + Style.RESET_ALL)
                    
                    
    
    @staticmethod
    def display_user_menu(library : Library):
        keep_going = True
        while (keep_going):
            print(Fore.BLUE + "1 - Exibir Coleção")
            print("2 - Devolver Livro")
            print("3 - Pegar Livro Emprestado")
            print("4 - Renovar Livro")
            print("5- Sair do Menu de Usuário" )
            
            option = int(input(Fore.YELLOW + "Digite uma opção (1 - 3): " + Style.RESET_ALL))
            
            match option:
                case 1:
                    library.show_collection()
                    
                case 2:
                    cpf = int(input("Digite o cpf do usuário: "))
                    book_id  = int(input("Digite o id do livro: "))
                    library.return_book(cpf, book_id)
                    
                case 3:
                    book = Menu.input_book_details()
                    user = Menu.input_user_details()
                    library.loan_book(user, book, datetime.today())
                    
                case 4:
                    book_id  = int(input("Digite o id do livro: "))
                    library.renew_book(book_id)
                    
                case 5:
                    keep_going = False
                    
                case _:
                    print(Fore.RED + "Opção inválida. Por favor, tente novamente." + Style.RESET_ALL)

    @staticmethod
    def display_admin_menu(library : Library):
        keep_going = True
        while (keep_going):
            print(Fore.BLUE + "1 - Registar Usuário")
            print("2 - Remover Usuário")
            print("3 - Adicionar Livro")
            print("4 - Remover Livro")
            print("5 - Sair do Menu de Administrador")
            
            option = int(input(Fore.YELLOW + "Digite uma opção (1 - 3): " + Style.RESET_ALL))
            
            match option:
                case 1:
                    user = Menu.input_user_details()
                    library.add_user(user)
                    
                case 2:
                    user = Menu.input_user_details()
                    library.remove_user(user)
                    
                case 3:
                    book = Menu.input_book_details()
                    library.add_book(book)
                    
                case 4:
                    book = Menu.input_book_details()
                    library.remove_book(book)

                case 5:
                    keep_going = False
                    
                case _:
                    print(Fore.RED + "Opção inválida. Por favor, tente novamente." + Style.RESET_ALL)
    
    @staticmethod
    def input_user_details() -> User:
        cpf = int(input("Digite o cpf do usuário: "))
        password = input("Digite a senha do usuário: ")
        name = input("Digite o nome do usuário")
        is_admin = bool(input("Digite se o usuário é administrador: "))
        email = input("Digite o email do usuário: ")
        return User(cpf, name, email, password, is_admin)
    
    @staticmethod
    def input_book_details() -> Book:
        id  = int(input("Digite o id do livro: "))
        title = input("Digite o título do livro: ")
        author = input("Digite o autor do livro: ")
        genre = input("Digite o gênero do livro: ")
        return Book(id, title, author, genre)
        
        
        
        
        
    
    

            