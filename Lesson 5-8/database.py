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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contact_id INTEGER NOT NULL,
            message_text TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (contact_id) REFERENCES contacts(id) ON DELETE CASCADE
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

def add_message(contact_id, text):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (contact_id, message_text) VALUES (?, ?)", (contact_id, text))
    conn.commit()
    conn.close()

def get_messages_by_contact(contact_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT message_text, timestamp
        FROM messages
        WHERE contact_id = ?
        ORDER BY timestamp DESC
    """, (contact_id,))
    result = cursor.fetchall()
    conn.close()
    return result