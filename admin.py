import sqlite3
from db_setup import DatabaseSetup
from database import DatabaseManager

def add_item(db):
    item_type = input("Enter item type (Book/Magazine): ").strip().capitalize()
    if item_type not in['Book', 'Magazine']:
        print("Invaid type. Must be Book or Magazine")
        return
    
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    description = input("Enter description (optionla): ").strip()
    if not title or not author:
        print("Title and author cannot be empty")
        return
    
    try:
        item_id = db.add_item(item_type, title, author, description)
        if item_id:
            print(f"{item_type} '{title}' added successfully with ID {item_id}.")
    except sqlite3.Error as e:
        print(f"Error adding item: {e}")

def main():
    db_setup = DatabaseSetup('library.db')
    db_setup.connect()
    db = DatabaseManager(db_setup.conn, db_setup.cur)

    while True:
        print("\nAdmin Panel Option: ")
        print("1. Add a new item (Book or Magazine)")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(db)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    db_setup.close()

if __name__ == "__main__":
    main()