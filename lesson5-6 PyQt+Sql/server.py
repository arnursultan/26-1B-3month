import os
import socket
import threading
import database
import json

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    data = conn.recv(4096).decode()
    if not data:
        return
    parts = data.strip().split('|')

    if parts[0] == "add":
        name, phone, email = parts[1], parts[2], parts[3]
        database.add_contact(name, phone, email)
        conn.sendall("OK".encode())

    elif parts[0] == "get_all":
        contacts = database.get_all_contacts()
        conn.sendall(json.dumps(contacts).encode())

    elif parts[0] == "delete":
        contact_id = int(parts[1])
        database.delete_contact(contact_id)
        conn.sendall("OK".encode())

    elif parts[0] == "search":
        name = parts[1]
        results = database.search_contacts(name)
        conn.sendall(json.dumps(results).encode())

    elif parts[0] == "update":
        contact_id, name, phone, email = int(parts[1]), parts[2], parts[3], parts[4]
        database.update_contact(contact_id, name, phone, email)
        conn.sendall("OK".encode())

    elif parts[0] == "exit":
        conn.sendall("OK".encode())
        conn.close()
        print("Сервер завершает работу...")
        os._exit(0)

    else:
        conn.sendall("UNKNOWN_COMMAND".encode())

    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Сервер запущен на {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()