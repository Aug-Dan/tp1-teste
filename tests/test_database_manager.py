from src.DatabaseManager import DatabaseManager

def test_database_manager_singleton():
    # Cria duas instancias da classe DatabaseManager
    db_manager1 = DatabaseManager()
    db_manager2 = DatabaseManager()

    # checa se as duas são iguais
    assert db_manager1 is db_manager2
