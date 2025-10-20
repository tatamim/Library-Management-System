Python & SQL Command-Line Library Management System

Overview

This is a command-line application that allows users to manage a library's inventory, 
including adding items like books and magazines, borrowing, and returning them using Python 3 and SQLite.
The project demonstrates all pillars of Object-Oriented Programming (OOP):





Encapsulation: Data and methods are bundled in classes (e.g., LibraryItem encapsulates title, author, etc.).



Abstraction: Abstract base class (LibraryItem) hides implementation details and provides a blueprint.



Inheritance: Subclasses like Book and Magazine inherit from LibraryItem.



Polymorphism: Subclasses override methods (e.g., display_info()) to provide specific behavior.

Setup Instructions

Prerequisites:





Python 3.x installed on your system.



No additional server setup is required for SQLite as it is built into Python.

Project Structure:





main.py: The entry point for users.



admin.py: For admin to add library items.



database.py: Manages database connections and queries.



models.py: Defines the LibraryItem, Book, Magazine, and BorrowRecord classes.



schema.sql: Defines the database schema.



sample_data.sql: Populates the database with sample items.

Installation:





Ensure all files are in the same directory.



No external dependencies are required beyond Python's standard library.

Initialize the Database:





Run python main.py for the first time. The application will create library.db and populate it with tables and sample data from schema.sql and sample_data.sql.

Running the Application:





For users: Execute python main.py in your terminal. Follow prompts to borrow/return items or view inventory.



For admin: Execute python admin.py to add new items.

Usage

In main.py:





Enter your name.



Choose options: "View available items", "Borrow an item", "Return an item", "View borrow history", or "Exit".



Select items by number.

In admin.py:





Add new books or magazines with details.

Notes





The database (library.db) will be created automatically if it doesn't exist.



Ensure schema.sql and sample_data.sql are in the same directory as main.py, or adjust the paths accordingly.

Bonus Features





View borrow history for a user.



Basic error handling for invalid inputs.

Contributing

This is a student project demonstrating OOP pillars. For enhancements, contact the developer.
