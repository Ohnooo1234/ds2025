import socket

def client(server_host='127.0.0.1', server_port=13112, namefile='ngoctung.txt'):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    print(f"Connected To Server {server_host}:{server_port}")
    client_socket.sendall(namefile.encode())
    with open(f"received_{namefile}", 'wb') as file:
        while (chunk := client_socket.recv(1024)):
            if b"ERROR" in chunk:  
                print(chunk.decode())
                break
            file.write(chunk)
    print(f"File Transfer Complete: received_{namefile}")
    client_socket.close()

if __name__ == "__main__":
    client(namefile='ngoctung.txt')
