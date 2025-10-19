from db_setup import DatabaseSetup
from database import DatabaseManager
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
        print("Initializing database....")
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
            
            elif choice == '2':
                items = db.get_all_items()
                available_items = [item for item in items if item.available]
                if not available_items:
                    print("No items available to borrow.")
                    continue
                print("\nAvailable Items to Borrow:")
                for i,item in enumerate(available_items, 1):
                    print(f"{i}. ", end="")
                    item.display_info()
                try:
                    item_num = int(input("Select an item by number to borrow: ").strip())
                    if 1 <= item_num <= len(available_items):
                        selected_item = available_items[item_num - 1]
                        if db.borrow_item(user_name, selected_item.item_id):
                            print(f"You have borrowed: {selected_item.title}")
                        else:
                            print("Unable to borrow the item.")
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Please enter a valid number.")
            
            elif choice == '3':
                history = db.get_borrow_history(user_name)
                borrowed = [record for record in history if record.return_date is None]
                if not borrowed:
                    print("You have no items to return.")
                    continue
                print("\nYour Borrowed Items:")
                items = db.get_all_items()
                for i, record in enumerate(borrowed, 1):
                    item = next((it for it in items if it.item_id == record.item_id), None)
                    if item:
                        print(f"{i}. ", end="")
                        item.display_info()
                try:
                    item_num = int(input("Select an item by number to return: ").strip())
                    if 1 <= item_num <= len(borrowed):
                        selected_record = borrowed[item_num - 1]
                        if db.return_item(user_name, selected_record.item_id):
                            print("Item returned successfully.")
                        else:
                            print("Unable to return the item.")
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == '4':
                history = db.get_borrow_history(user_name)
                if not history:
                    print("No borrow history.")
                    continue
                print("\nYour Borrow History:")
                items = db.get_all_items()
                for record in history:
                    item = next((it for it in items if it.item_id == record.item_id), None)
                    if item:
                        item.display_info()
                        print(f"  Borrowed on: {record.borrow_date}, Returned on: {record.return_date if record.return_date else 'Not returned yet'}")

            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter 1-5.")

        another = input("Do you want to start over? (yes/no): ").strip().lower()
        if another not in ['yes', 'y']:
            break

    db_setup.close()

if __name__ == "__main__":
    main()

    