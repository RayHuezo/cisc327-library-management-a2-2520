import pytest
from library_service import (
    get_patron_status_report
)

def test_valid_patron_id():
    """Tests for valid patron ID"""
    success, message = get_patron_status_report(patron_id= "123456")

    assert success == True
    assert "ID is 6 digits"

def test_invalid_patron_id_too_short():
    """Tests for invalid patron ID that is too short"""
    success, message = get_patron_status_report(patron_id="123")

    assert success == False
    assert "ID must be 6 digits"

def test_invalid_patron_id_too_long():
    """Tests for invalid patron ID that is too long"""
    success, message = get_patron_status_report(patron_id="12345678")

    assert success == False
    assert "ID must be 6 digits"

def test_invalid_patron_id_blank():
    """Tests for invalid patron ID that is blank"""
    success, message = get_patron_status_report(patron_id=" ")

    assert success == False
    assert "ID must be 6 digits"