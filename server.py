import socket

def main():
    host = 'localhost'
    port = 13000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Servidor escutando em {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexão recebida de {client_address}")

        request = client_socket.recv(1024).decode()
        print(f"Requisição do cliente:\n{request}")

        filename = request.split()[1].lstrip('/')
        if filename == '':
            filename = 'index.html'

        try:
            file = open(filename, 'rb')
            response_data = file.read()
            file.close()

            response_server = 'HTTP/1.1 200 OK\n'

            if filename.endswith('.jpg'):
                type = 'image/jpg'
            else:
                type = 'text/html'

            response_server += 'Content-Type: '+str(type)+'\n\n'

        except Exception as e:
            print("-")
            response_server = 'HTTP/1.1 404 Not Found\n\n'
            response_data = '<html><body>Error 404: File not found</body></html>'.encode('utf-8')

        final_response = response_server.encode('utf-8') + response_data
        client_socket.sendall(final_response)


        client_socket.close()

if __name__ == "__main__":
    main()
