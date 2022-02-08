import sqlite3

class DB:
    def __init__(self):
        self.con = sqlite3.connect('books.db')
        self.cur = self.con.cursor()
        self.cur.execute(
                "CREATE TABLE IF NOT EXISTS Books ( \
                    id INTEGER PRIMARY KEY AUTOINCREMENT \
                    isbn INTEGER, \
                    title TEXT, \
                    author TEXT, \
                    pagesread INTEGER, \
                    totalpages INTEGER, \
                    averagerating INTEGER \
                    )"
                )
        self.conn.commit()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def view(self):
        self.curr.execute("SELECT * FROM Books")
        row = self.cur.fetchall()
        return row

    def insert(self, isbn):
        self.cur.execute(
                "INSERT INTO Books VALUES (?)", (isbn))
        self.conn.commit()
        self.view()

    def update(self, ISBN, title, author, pagesread):
        self.cur.execute(
            "UPDATE Books SET title=?, author=?, pagesread=? WHERE id=?", 
                (title, author, pagesread, isbn))

    def search(self, title="", author=""):
        self.cur.execute(
            "SELECT * FROM Books Where title=? OR author=?", (title, author))
        row = self.cur.fetchall()
        return row



