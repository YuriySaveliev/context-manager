import sqlite3


class ContextManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            self.connection.commit()
        else:
            print(exc_val)
            self.connection.rollback()

        self.connection.close()

        return True


cm = ContextManager('test.db')
with cm:
    cm.cursor.execute("CREATE TABLE products(name text, quantity integer, price real)")
    cm.cursor.execute("INSERT INTO products VALUES ('Potato', 10, 11.50)")
