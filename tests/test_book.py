import pytest
from src.Book import Book


@pytest.fixture
def sample_book():
    return Book(id=1, title="Sample Book", author="Sample Author", genre="Sample Genre")

def test_get_id(sample_book):
    assert sample_book.get_id() == 1

def test_get_title(sample_book):
    assert sample_book.get_title() == "Sample Book"

def test_get_author(sample_book):
    assert sample_book.get_author() == "Sample Author"

def test_get_genre(sample_book):
    assert sample_book.get_genre() == "Sample Genre"

def test_get_borrowed(sample_book):
    assert sample_book.get_borrowed() == False
