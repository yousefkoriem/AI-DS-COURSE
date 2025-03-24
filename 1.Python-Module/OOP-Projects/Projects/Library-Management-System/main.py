from datetime import date
from enum import Enum

# Enumeration
class BookFormat(Enum):
    HARDCOVER = "Hardcover"
    PAPERBACK = "Paperback"
    AUDIOBOOK = "Audiobook"
    EBOOK = "Ebook"
    NEWSPAPER = "Newspaper"
    MAGAZINE = "Magazine"
    JOURNAL = "Journal"

class BookStatus(Enum):
    AVAILABLE = "Available"
    RESERVED = "Reserved"
    LOANED = "Loaned"
    LOST = "Lost"

class ReservationStatus(Enum):
    WAITING = "Waiting"
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELED = "Canceled"
    NONE = "None"

class AccountStatus(Enum):
    ACTIVE = "Active"
    CLOSED = "Closed"
    CANCELED = "Canceled"
    BLACKLISTED = "Blacklisted"
    NONE = "None"

# Data Types
class Address:
    def __init__(self, street: str, city: str, state: str, zipcode: str, country: str):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country

class Person:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone



class Book:
    def __init__(self, isbn: str, title: str, subject: str, publisher: str, language: str, num_pages: int):
        self.isbn = isbn
        self.title = title
        self.subject = subject
        self.publisher = publisher
        self.language = language
        self.num_pages = num_pages

    def get_title(self) -> str:
        return self.title

class Rack:
    def __init__(self, number: int, location_identifier: str):
        self.number = number
        self.location_identifier = location_identifier

class BookItem(Book):
    def __init__(self, barcode: str, is_reference_only: bool, borrowed: date, due_date: date, price: float, book_format: BookFormat,
                 purchase_date: date, publication_date: date, checkout: bool, **kwargs):
        super().__init__(**kwargs)
        self.barcode = barcode
        self.is_reference_only = is_reference_only
        self.borrowed = borrowed
        self.due_date = due_date
        self.price = price
        self.book_format = book_format
        self.purchase_date = purchase_date
        self.publication_date = publication_date
        self.checkout = checkout


class Author:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def get_name(self) -> str:
        return self.name


class Library:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def get_address(self) -> Address:
        return self.address

class Account(Person):
    def __init__(self, id: str, password: str, status: AccountStatus, person: Person):
        super().__init__(person.name, person.email, person.phone)
        self.id = id
        self.password = password
        self.status = status

    def reset_password(self):
        pass  # Implement reset password functionality

class Member(Account):
    def __init__(self, date_of_membership: date, total_books_checked_out: int, **kwargs):
        super().__init__(**kwargs)
        self.date_of_membership = date_of_membership
        self.total_books_checked_out = total_books_checked_out

    def get_total_checked_out_books(self) -> int:
        return self.total_books_checked_out

class Librarian(Account):
    def add_book_item(self) -> bool:
        pass

    def block_member(self) -> bool:
        pass

    def unblock_member(self) -> bool:
        pass

class LibraryCard:
    def __init__(self, card_number: str, barcode: str, issued_at: date, active: bool):
        self.card_number = card_number
        self.barcode = barcode
        self.issued_at = issued_at
        self.active = active

    def is_active(self) -> bool:
        return self.active

class BarcodeReader:
    def __init__(self, id: str, registered_at: date, active: bool):
        self.id = id
        self.registered_at = registered_at
        self.active = active

    def is_active(self) -> bool:
        return self.active



class BookReservation:
    def __init__(self, creation_date: date, status: ReservationStatus, member: Member):
        self.creation_date = creation_date
        self.status = status
        self.member = member

    def get_status(self) -> ReservationStatus:
        return self.status

    def fetch_reservation_details(self):
        pass

class BookLending:
    def __init__(self, creation_date: date, due_date: date, return_date: date):
        self.creation_date = creation_date
        self.due_date = due_date
        self.return_date = return_date

    def get_return_date(self) -> date:
        return self.return_date

class Fine:
    def __init__(self, amount: float):
        self.amount = amount

    def get_amount(self) -> float:
        return self.amount


class FineTransaction:
    def __init__(self, creation_date: date, amount: float):
        self.creation_date = creation_date
        self.amount = amount

    def initiate_transaction(self) -> bool:
        pass

class CreditCardTransaction(FineTransaction):
    def __init__(self, name_on_card: str, **kwargs):
        super().__init__(**kwargs)
        self.name_on_card = name_on_card

class CheckTransaction(FineTransaction):
    def __init__(self, bank_name: str, check_number: str, **kwargs):
        super().__init__(**kwargs)
        self.bank_name = bank_name
        self.check_number = check_number

class CashTransaction(FineTransaction):
    def __init__(self, cash_tendered: float, **kwargs):
        super().__init__(**kwargs)
        self.cash_tendered = cash_tendered


class Notification:
    def __init__(self, notification_id: int, created_on: date, content: str):
        self.notification_id = notification_id
        self.created_on = created_on
        self.content = content

    def send_notification(self) -> bool:
        pass

class PostalNotification(Notification):
    def __init__(self, address: Address, **kwargs):
        super().__init__(**kwargs)
        self.address = address

class EmailNotification(Notification):
    def __init__(self, email: str, **kwargs):
        super().__init__(**kwargs)
        self.email = email
