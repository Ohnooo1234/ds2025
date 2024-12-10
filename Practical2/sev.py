from xmlrpc.server import SimpleXMLRPCServer
import os
def serve_file(namefile):
    try:
        with open(namefile, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        return f"ERROR: File '{namefile}' Not Found.".encode()
def server(host='127.0.0.1', port=13112):
    server = SimpleXMLRPCServer((host, port))
    print(f"RPC Server Listening On {host}:{port}")
    server.register_function(serve_file, "serve_file")
    server.serve_forever()
if __name__ == "__main__":
    server()
