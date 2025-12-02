import re
from playwright.sync_api import Page, expect

def test_add_book(page: Page):
    page.goto("http://localhost:5000")

    # Click the Add New Book link.
    page.get_by_role("link", name="➕ Add New Book").click()

    # Expects page to have a heading with the name of ➕ Add New Book
    expect(page.get_by_role("heading", name="➕ Add New Book")).to_be_visible()

    # Fill the title textbox
    page.get_by_role("textbox", name = "Title *").fill("Animal Farm")

    # Fill the author textbox
    page.get_by_role("textbox", name="Author *").fill("George Orwell")

    # Fill the ISBN textbox
    page.get_by_role("textbox", name="ISBN *").fill("9876543211234")

    # Fill the total copies textbox
    page.get_by_role("textbox", name="Total Copies *").fill("3")

    # Click the add book to catalog link.
    page.get_by_role("link", name="Add Book to Catalog").click()

    # Expects page to have a heading with the name of ➕ Add New Book
    expect(page.get_by_role("heading", name="Book 'Animal Farm' has been successfully added to the catalog.")).to_be_visible()

