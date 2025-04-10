import socket

HOST = '127.0.0.1'
PORT = 65432

def send_command(command: str) -> str:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(command.encode())
            response = s.recv(4096).decode()
            return response
    except Exception as e:
        return f"ERROR|{str(e)}"

def shutdown_server():
    return send_command("exit")