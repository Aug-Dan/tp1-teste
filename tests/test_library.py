import pytest
import unittest
from unittest.mock import MagicMock

from src.Library import Library
from src.User import User

@pytest.fixture
def setUp():
    # Cria um mock para o database manager
    mock_db = MagicMock()
    library = Library(mock_db)
    return library, mock_db

def test_add_user(setUp):
    library, mock_db = setUp
    
    user = User(CPF="12345678900", name="Test User", email="test@example.com", 
                password="password123", is_admin=False)
    
    library.add_user(user)
        
    # Verifica se o método execute_query foi chamado com a consulta SQL correta e os parâmetros esperados
    mock_db.execute_query.assert_called_once_with(
            "INSERT INTO users (cpf, name, email, password, is_admin, current_loans_count) VALUES (?, ?, ?, ?, ?, ?)",
            (user.CPF, user.name, user.email, user.password, user.is_admin, user.current_loans_count)
        )
        
    # Verifica se o método commit foi chamado uma vez
    mock_db.commit.assert_called_once()



