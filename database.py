import sqlite3
def setup_database():

 conn = sqlite3.connect('restraunt.db')
 cursor = conn.cursor()

 cursor.execute("""CREATE TABLE IF NOT EXISTS menu_items(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT,
 price INTEGER)""")

 items = [
    ('Burger', 50),
    ('Pizza', 100),
    ('Pasta',80),
    ('Sandwich',40)
 ]

 cursor.execute("SELECT COUNT(*) FROM menu_items")
 count = cursor.fetchone()[0]
 if count==0:
   cursor.executemany("INSERT INTO menu_items (name, price) VALUES (?, ?)"
   ,items)

 conn.commit()
 conn.close()

