import sqlite3

def connect_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        );
    """)
    conn.commit()
    return conn

def add_contact(name, phone, email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()

def get_all_contacts():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    result = cursor.fetchall()
    conn.close()
    return result

def search_contacts(name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
    result = cursor.fetchall()
    conn.close()
    return result

def delete_contact(contact_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()

def update_contact(contact_id, name, phone, email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE contacts
        SET name = ?, phone = ?, email = ?
        WHERE id = ?
    """, (name, phone, email, contact_id))
    conn.commit()
    conn.close()