from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_id, title, author, description, available):
        self._item_id = item_id # Encapsulation: protected attribute
        self._title = title
        self._author = author
        self._description = description
        self._available = available

    @property
    def item(self):
        return self._item_id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def description(self):
        return self._description

    @property
    def available(self):
        return self._available

    @abstractmethod
    def display_info(self):
        """Abtraction method to display item info """
        pass

class Book(LibraryItem):
    def display_info(self):
        # Polymorphism: overriding the abstract method
        print(f"Book: {self.title} by {self.author} - {self.description} (Available: {'Yes' if self.available else 'No'})")

class Magazine(LibraryItem):
    def display_info(self):
        # Polymorphism: overriding the abstract method
        print(f"Magazine: {self.title} by {self.author} - {self.description} (Available: {'Yes' if self.available else 'No'})")

class BorrowRecord:
    def __init__(self, record_id, user_name, item_id, borrow_date, return_date=None):
        self.record_id = record_id
        self.user_name = user_name
        self.item_id = item_id
        self.borrow_date = borrow_date
        self.return_date = return_date