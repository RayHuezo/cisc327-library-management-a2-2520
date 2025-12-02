import pytest
from library_service import (
    add_book_to_catalog
)

def test_invaild_title_too_long():
    """Tests for invalid book title that's too long"""
    success, message = add_book_to_catalog(title= "abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxy", author= "Test Author", isbn= "1234567890123", total_copies= 5)

    assert success == False
    assert "Title max 200 characters" in message

def test_invaild_author_too_long():
    """Tests for invalid author that's too long"""
    success, message = add_book_to_catalog(title= "Book Title", author= "abcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxyabcdefghijklmnopqrstuvwxy", isbn= "1234567890123", total_copies= 5)

    assert success == False
    assert "Author max 100 characters" in message


def test_valid_isbn():
    """Tests for valid ISBN"""
    success, message = add_book_to_catalog("Test Book", "Test Author", "1234567891234", 5)

    assert success == True
    assert "ISBN is 13 digits" in message

def test_invalid_negative_copies():
    """Tests for invalid negative number of book copies"""
    success, message = add_book_to_catalog("Test Book", "Test Author", "123456789123456", -2)

    assert success == False
    assert "Number of copies must be positive" in message
