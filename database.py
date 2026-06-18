import sqlite3

def connect_db():
    conn = sqlite3.connect("todo.db")
    return conn


def create_table():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()