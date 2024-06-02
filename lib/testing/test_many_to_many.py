from many_to_many import Author, Book, Contract
import pytest

def test_author_init():
    author = Author("John Doe")
    assert author.name == "John Doe"

def test_book_init():
    book = Book("Python Programming")
    assert book.title == "Python Programming"

def test_contract_init():
    author = Author("Jane Smith")
    book = Book("Data Science Essentials")
    contract = Contract(author, book, "2024-06-03", 10)
    assert contract.author == author
    assert contract.book == book
    assert contract.date == "2024-06-03"
    assert contract.royalties == 10

def test_author_contracts():
    author = Author("John Doe")
    book1 = Book("Python Programming")
    book2 = Book("Data Science Essentials")
    contract1 = author.sign_contract(book1, "2024-06-01", 15)
    contract2 = author.sign_contract(book2, "2024-06-02", 20)
    assert author.contracts() == [contract1, contract2]

def test_author_books():
    author = Author("Jane Smith")
    book1 = Book("Python Programming")
    book2 = Book("Data Science Essentials")
    author.sign_contract(book1, "2024-06-01", 15)
    author.sign_contract(book2, "2024-06-02", 20)
    assert author.books() == [book1, book2]

def test_author_total_royalties():
    author = Author("John Doe")
    book1 = Book("Python Programming")
    book2 = Book("Data Science Essentials")
    author.sign_contract(book1, "2024-06-01", 15)
    author.sign_contract(book2, "2024-06-02", 20)
    assert author.total_royalties() == 35

def test_contract_by_date():
    author = Author("Jane Smith")
    book1 = Book("Python Programming")
    book2 = Book("Data Science Essentials")
    contract1 = author.sign_contract(book1, "2024-06-01", 15)
    contract2 = author.sign_contract(book2, "2024-06-02", 20)
    contract3 = author.sign_contract(book2, "2024-06-02", 25)
    contracts = Contract.contracts_by_date("2024-06-02")
    assert len(contracts) == 2
    assert contract2 in contracts
    assert contract3 in contracts
