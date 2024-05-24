from src.Library import Library
from src.User import User
from src.Loan import Loan
from src.AuthenticationSystem import AuthenticationSystem, UserType
from DatabaseManager import DatabaseManager

from colorama import Fore, Style

class Menu:
    @staticmethod
    def display_welcome():
        KeepGoing = True
        print(Fore.GREEN + "Seja Bem Vindo ao Sistema" + Style.RESET_ALL)
        
        while (KeepGoing):
            print(Fore.BLUE + "1 - Exibir Coleção")
            print("2 - Logar no sistema")
            print("3 - Sair" + Style.RESET_ALL)
            
            option = int(input(Fore.YELLOW + "Digite uma opção (1 - 3): " + Style.RESET_ALL))
            
            match option:
                case 1:
                    Library.show_collection()
                case 2: 
                    Menu.display_login()
                case 3:
                    KeepGoing = False
                case _:
                    print(Fore.RED + "Opção inválida. Por favor, tente novamente." + Style.RESET_ALL)
                    
    @staticmethod
    def display_login():
        
        # Pede para o usuário logar no sistema
        auth = AuthenticationSystem()
        try:
            result = auth.login()
            if (result == UserType.Student):
                Menu.display_user_menu()
            elif (result == UserType.Admin):
                Menu.display_admin_menu()
        except Exception as e:
            print(f"Ocorreu um erro durante o login: {e}")
                    
    
    @staticmethod
    def display_user_menu():
        KeepGoing = True
        while (KeepGoing):
            print(Fore.BLUE + "1 - Exibir Coleção")
            print("2 - Devolver Livro")
            print("3 - Pegar Livro Emprestado")
            print("4 - Renovar Livro")
            print("5- Sair do Menu de Usuário" )
            
            option = int(input(Fore.YELLOW + "Digite uma opção (1 - 3): " + Style.RESET_ALL))
            
            match option:
                case 1:
                    Library.show_collection()
                case 2: 
                    Library.return_book()
                case 3:
                    Library.loan_book()
                case 4:
                    Library.renew_book()
                case 5:
                    KeepGoing = False
                case _:
                    print(Fore.RED + "Opção inválida. Por favor, tente novamente." + Style.RESET_ALL)

    @staticmethod
    def display_admin_menu():
        KeepGoing = True
        while (KeepGoing):
            print(Fore.BLUE + "1 - Registar Usuário")
            print("2 - Remover Usuário")
            print("3 - Adicionar Livro")
            print("4 - Remover Livro")
            print("5 - Sair do Menu de Administrador")
            
            option = int(input(Fore.YELLOW + "Digite uma opção (1 - 3): " + Style.RESET_ALL))
            
            match option:
                case 1:
                    Library.add_user()
                    pass
                case 2: 
                    Library.remove_user()
                    pass
                case 3:
                    Library.add_book()
                case 4:
                    Library.remove_book()
                case 5:
                    KeepGoing = False
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
        
        
        
        
        
    
    

            