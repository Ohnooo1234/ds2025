import socket

def server(host='127.0.0.1', port=13112):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server Listening On {host}:{port}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected By Address: {addr}")

        # Receive file name from client
        namefile = conn.recv(512).decode()
        print(f"Client Requested File: {namefile}")

        try:
            with open(namefile, 'rb') as file:
                while (chunk := file.read(1024)):
                    conn.sendall(chunk)
            print("File Sent Completed!")
        except FileNotFoundError:
            conn.sendall(b"ERROR: File Not Found.")
            print("Not File Sent To Client")
        
        conn.close()

if __name__ == "__main__":
    server()
