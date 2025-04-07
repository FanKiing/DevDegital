import sqlite3


class CRUDOperations:
    def __init__(self):
        self.conn = sqlite3.connect("app.db")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def create(self, name, email, phone):
        query = "INSERT INTO users (name, email, phone) VALUES (?, ?, ?)"
        self.conn.execute(query, (name, email, phone))
        self.conn.commit()

    def read_all(self):
        query = "SELECT * FROM users"
        return self.conn.execute(query).fetchall()

    def update(self, record_id, name, email, phone):
        query = "UPDATE users SET name = ?, email = ?, phone = ? WHERE id = ?"
        self.conn.execute(query, (name, email, phone, record_id))
        self.conn.commit()

    def delete(self, record_id):
        query = "DELETE FROM users WHERE id = ?"
        self.conn.execute(query, (record_id,))
        self.conn.commit()
