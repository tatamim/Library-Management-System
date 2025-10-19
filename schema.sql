CREATE TABLE library_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL CHECK (type IN ('Book', 'Magazine')),
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    description TEXT,
    available INTEGER NOT NULL CHECK (available IN (0, 1))
);

CREATE TABLE borrow_records (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    item_id INTEGER NOT NULL,
    borrow_date TIMESTAMP default CURRENT_TIMESTAMP,
    return_date TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES library_items(item_id) ON DELETE CASCADE
);