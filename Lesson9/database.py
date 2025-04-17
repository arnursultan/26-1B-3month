import sqlite3
from datetime import datetime

def get_connection():
    return sqlite3.connect("tasks.db")

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL DEFAULT 'не выполнено',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def add_task(title, description, status="не выполнено"):
    conn = get_connection()
    cursor = conn.cursor()
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO tasks (title, description, status, created_at) VALUES (?, ?, ?, ?)",
                   (title, description, status, created_at))
    conn.commit()
    conn.close()

def get_tasks(status_filter=None):
    conn = get_connection()
    cursor = conn.cursor()
    if status_filter and status_filter != "все":
        cursor.execute("SELECT * FROM tasks WHERE status = ? ORDER BY created_at DESC", (status_filter,))
    else:
        cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def search_tasks(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM tasks WHERE title LIKE ? OR status LIKE ?
        ORDER BY created_at DESC
    """, (f"%{query}%", f"%{query}%"))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def update_task(task_id, title, description, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tasks SET title=?, description=?, status=? WHERE id=?
    """, (title, description, status, task_id))
    conn.commit()
    conn.close()

def get_task_by_id(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    task = cursor.fetchone()
    conn.close()
    return task
