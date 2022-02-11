import sqlite3

class DB:
    def __init__(self):
        self.con = sqlite3.connect('books.db')
        self.cur = self.con.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Books \
            (id INTEGER PRIMARY KEY AUTOINCREMENT, \
            isbn INTEGER, \
            title TEXT, \
            author TEXT, \
            pagesread INTEGER, \
            totalpages INTEGER)"
                         )
        self.con.commit()

    def __del__(self):
        self.con.commit()
        self.con.close()

    def view(self):
        self.cur.execute("SELECT * FROM Books")
        row = self.cur.fetchall()
        return row

    def insert(self, isbn, title, author, pagesread, pagestot):
        self.cur.execute(
                "INSERT INTO Books VALUES (NULL,?,?,?,?,?)", (isbn,title,author,pagesread,pagestot))
        self.con.commit()
        self.view()

    def update(self, ISBN, title, author, pagesread):
        self.cur.execute(
            "UPDATE Books SET title=?, author=?, pagesread=? WHERE id=?", 
                (title, author, pagesread, isbn))

    def search(self, isbn="", title="", author=""):
        self.cur.execute(
            "SELECT * FROM Books WHERE isbn=? OR title=? OR author=?", (isbn, title, author))
        row = self.cur.fetchall()
        return row

