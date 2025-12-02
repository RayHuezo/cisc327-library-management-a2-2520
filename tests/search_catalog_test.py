import pytest
from library_service import (
    search_books_in_catalog
)

def test_valid_search_term_title():
    """Tests for valid search term"""
    success, message = search_books_in_catalog(search_term= "Book Title", search_type= "Title")

    assert success == True
    assert "Valid search term" in message

def test_valid_search_term_author():
    """Tests for valid search term"""
    success, message = search_books_in_catalog(search_term="Book Author", search_type="Author")

    assert success == True
    assert "Valid search term" in message

def test_invalid_search_term_isbn():
    """Tests for invalid ISBN"""
    success, message = search_books_in_catalog(search_term="Book Title", search_type="ISBN")

    assert success == False
    assert "ISBN must be 13 digits" in message

def test_valid_search_term_isbn():
    """Tests for valid ISBN"""
    success, message = search_books_in_catalog(search_term="1234567891234", search_type="ISBN")

    assert success == True
    assert "Valid ISBN" in message