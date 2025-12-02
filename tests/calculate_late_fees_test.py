import pytest
from library_service import (
    calculate_late_fee_for_book
)

def test_valid_patron_id():
    """Tests for valid patron ID"""
    success, message = calculate_late_fee_for_book(patron_id= "123456", book_id= 1234567891234)

    assert success == True
    assert "Patron ID is 6 digits" in message


def test_invalid_book_id_too_long():
    """Tests for invalid book ID that is too long"""
    success, message = calculate_late_fee_for_book(patron_id= "123456", book_id= 12345678912345678)

    assert success == False
    assert "Book ID must be 13 digits" in message


def test_invalid_patron_id_too_long():
    """Tests for invalid patron ID that is too long"""
    success, message = calculate_late_fee_for_book(patron_id= "12345678", book_id= 1234567891234)

    assert success == False
    assert "Patron ID must be 6 digits" in message


def test_invalid_book_id_too_short():
    """Tests for invalid book ID that is too short"""
    success, message = calculate_late_fee_for_book(patron_id= "123456", book_id=123456)

    assert success == False
    assert "Book ID must be 13 digits" in message