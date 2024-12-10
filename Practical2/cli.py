from xmlrpc.client import ServerProxy, Binary

def client(server_host='127.0.0.1', server_port=13112, namefile='ngoctung.txt'):
    server_url = f"http://{server_host}:{server_port}"
    server = ServerProxy(server_url)
    print(f"Connected To RPC Server {server_host}:{server_port}")
    response = server.serve_file(namefile)
    if isinstance(response, Binary):
        response = response.data
    if response.startswith(b"ERROR"):
        print(response.decode())
    else:
        with open(f"received_{namefile}", 'wb') as file:
            file.write(response)
        print(f"File Transfer Complete: received_{namefile}")
if __name__ == "__main__":
    client(namefile='ngoctung.txt')
