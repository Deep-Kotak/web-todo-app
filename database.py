import sqlite3

def connect_db():
    return sqlite3.connect("todo.db")


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


def add_task(task):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks(task) VALUES(?)",
        (task,)
    )

    conn.commit()
    conn.close()

def delete_task(task_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

def complete_task(task_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status = 'Completed' WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

def get_stats():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tasks WHERE status='Completed'"
    )
    completed = cursor.fetchone()[0]

    pending = total - completed

    conn.close()

    return total, completed, pending

def search_tasks(keyword):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE task LIKE ?",
        ('%' + keyword + '%',)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks

def get_task_by_id(task_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    )

    task = cursor.fetchone()

    conn.close()

    return task


def update_task(task_id, updated_task):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET task = ? WHERE id = ?",
        (updated_task, task_id)
    )

    conn.commit()
    conn.close()

def get_tasks():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    tasks = cursor.fetchall()

    conn.close()

    return tasks