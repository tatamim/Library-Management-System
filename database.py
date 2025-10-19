import sqlite3
from models import LibraryItem, Book, Magazine, BorrowRecord

class DatabaseManager:
    def __init__(self, conn, cur):
        self.conn = conn 
        self.cur = cur 

    def get_all_items(self):
        try:
            self.cur.execute("SELECT item_id, type, title, author, description, available FROM library_items")
            rows = self.cur.fetchall()
            items = []
            for row in rows:
                if row[1] == 'Book':
                    items.append(Book(row[0], row[2], row[3], row[4], row[5]))
                elif row[1] == 'Magazine':
                    items.append(Book(row[0], row[2], row[3], row[4], row[5]))
            return items
        except sqlite3.Error as e:
            print(f"Error fetching items: {e}")
            return []
    
    def add_item(self, item_type, title, author, description):
        try:
            self.cur.execute("INSERT INTO library_items (type, title, author, description, available) VALUES (?, ?, ?, ?, 1)", (item_type, title, author, description))
            self.conn.commit()
            return self.cur.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding item: {e}")
            self.conn.rollback()
            return None
    
    def borrow_item(self, user_name, item_id):
        try:
            self.cur.execute("SELECT available FROM library_items WHERE item_id = ?", (item_id,))
            available = self.cur.fetchone()
            if not available or available[0] == 0:
                return False
            self.cur.execute("UPDATE library_items SET available = 0 WHERE item_id = ?", (item_id,))
            self.cur.execute("INSERT INTO borrow_records (user_name, item_id) VALUES (?, ?)", (user_name, item_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error borrowing item: {e}")
            self.conn.rollback()
            return False
    
    def return_item(self, user_name, item_id):
        try:
            self.cur.execute("SELECT record_id FROM borrow_records WHERE user_name = ? AND item_id = ? AND return_date IS NULL",
                             (user_name, item_id))
            record = self.cur.fetchone()
            if not record:
                return False
            self.cur.execute("UPDATE borrow_records SET return_date = CURRENT_TIMESTAMP WHERE record_id = ?", (record[0],))
            self.cur.execute("UPDATE library_items SET available = 1 WHERE item_id = ?", (item_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error returning item: {e}")
            self.conn.rollback()
            return False

    def get_borrow_history(self, user_name):
        try:
            self.cur.execute("SELECT record_id, item_id, borrow_date, return_date FROM borrow_records WHERE user_name = ?",
                             (user_name,))
            rows = self.cur.fetchall()
            return [BorrowRecord(row[0], user_name, row[1], row[2], row[3]) for row in rows]
        except sqlite3.Error as e:
            print(f"Error fetching borrow history:  {e}")
            return []
