import sqlite3

class ContextManager:
    def create_connection(self):
        self.connection = sqlite3.connect('test.db')
        self.cursor = self.connection.cursor()

        return self.cursor

    def exit(self):
        try:
            self.cursor.execute('''CREATE TABLE products(name text, quantity integer, price real)''')
            self.cursor.execute("INSERT INTO products VALUES ('Tomato', 50, 10.57)")
            self.connection.commit()
        except:
            print('Error!')
            self.connection.rollback()

        self.connection.close()

cm = ContextManager()
cursor = cm.create_connection()
cm.exit()
