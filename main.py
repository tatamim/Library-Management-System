from db_setup import DatabaseSetup
from database import DatabaseManager
from models import LibraryItem
import sqlite3


def main():
    db_setup = DatabaseSetup('library.db')
    is_new_db = db_setup.connect()

    try:
        db_setup.cur.execute("SELECT 1 FROM library_items LIMIT 1")
        table_exists = True
    except sqlite3.Error:
        table_exists = False
    
    if is_new_db or not table_exists:
        print("Initializing database...")
        try:
            db_setup.setup_database('schema.sql', 'sample_data.sql')
        except Exception as e:
            print(f"Failed to set up database: {e}.")
            db_setup.close()
            return
    
    db = DatabaseManager(db_setup.conn, db_setup.cur)

    while True:
        print("Wellcome to the Library Management System!")
        user_name = input("Please enter yoru name: ").strip()
        if not user_name:
            print("Name cannot be empty. Please try again.")
            continue

        while True:
            print("\nOptions:")
            print("1. View available items")
            print("2. Borrow an item")
            print("3. Return an item")
            print("4. View borrow history")
            print("5. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                items = db.get_all_items()
                if not items:
                    print("No items available.")
                    continue
                print("\nAvailable Items:")
                available_items = [item for item in items if item.available]
                for i, item in enumerate(available_items, 1):
                    print(f"{i}. ", end="")
                    item.display_info()   # Polymorphism in action
    