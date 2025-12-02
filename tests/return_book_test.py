import pytest
from library_service import (
    return_book_by_patron
)

def test_invalid_patron_id_too_long():
    """Tests for invalid patron ID that is too long"""
    success, message = return_book_by_patron(patron_id= "1234567", book_id= 1234567891234)

    assert success == False
    assert "Patron ID must be 6 digits" in message


def test_invalid_book_id_too_long():
    """Tests for invalid book ID that is too long"""
    success, message = return_book_by_patron(patron_id= "123456", book_id= 12345678912345678)

    assert success == False
    assert "Book ID must be 13 digits" in message


def test_valid_patron_id():
    """Tests for valid patron ID"""
    success, message = return_book_by_patron(patron_id= "123456", book_id= 1234567891234)

    assert success == True
    assert "Patron ID is 6 digits" in message


def test_valid_book_id():
    """Tests for valid book ID"""
    success, message = return_book_by_patron(patron_id= "123456", book_id=1234567891234)

    assert success == True
    assert "Book ID is 13 digits" in message