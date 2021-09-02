import sqlite3

class ContextManager:
    def create_connection(self):
        self.connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

    def exit(self):
        try:
            pass
        except:
            pass

        self.connection.close()

cm = ContextManager()