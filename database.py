import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bookmark (id INTEGER PRIMARY KEY, name text, link text, folder text)")
        self.conn.commit()

    def insert(self,name,link,folder):
        self.cur.execute("INSERT INTO bookmark VALUES (NULL,?,?,?)",(name,link,folder))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM bookmark")
        rows=self.cur.fetchall()
        return rows

    def search(self,name="",link="",folder=""):
        self.cur.execute("SELECT * FROM bookmark WHERE name=? OR link=? OR folder=?", (name,link,folder))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM bookmark WHERE id=?",(id,))
        self.conn.commit()

    def update(self,id,name,link,folder):
        self.cur.execute("UPDATE bookmark SET name=?, link=?, folder=? WHERE id=?",(name,link,folder,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

