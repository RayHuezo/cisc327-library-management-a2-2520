Ray Huezo - 20352520   
Group 2

# Implementation Status

| Function Name               | Implementation Status | Missing                                                                                                                            | 
|-----------------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------|
| add_book_to_catalog         | Complete              |
| borrow_book_by_patron       | Complete              |
| return_book_by_patron       | Partial               | Does not verify book, update available copies count, record return date, calculate and display late fees                           |
| calculate_late_fee_for_book | Partial               | Does not calculate late fee or return JSON response with with fee amount and days overdue                                          |
| search_books_in_catalog     | Partial               | Does not partial match book title or author, does not match ISBN, does not display matched books                                   |
| get_patron_status_report    | Partial               | There is no menu option for patron status report. No display of patron's currently borrowed books, late fees, or borrowing history | 

# Test Scrip Descriptions

Add book to Catalog: Tests for invalid title over 200 characters, invalid author over 100 characters, valid ISBN of 13 characters, and invalid negative number of copies. 

Borrow Book: Tests for invalid over 6 digit patron ID, invalid under 13 digit book ID, valid 6 digit patron ID, valid 13 digit book ID. 

Return Book: Tests for invalid over 6 digit patron ID, invalid over 13 digit book ID, valid 6 digit patron ID, valid 13 digit book ID. 

Calculate Late Fees: Tests for valid 6 digit patron ID, invalid over 13 digit book ID, invalid over 6 digit patron ID, invalid under 13 digit book ID. 

Search Book Catalog: Tests for valid search terms title and book, tests for valid and invalid ISBN. 

Patron Status Report: Tests for valid 6 digit patron ID, invalid over 6 digit patron ID, invalid under 6 digit patron ID, invalid blank patron ID. 


