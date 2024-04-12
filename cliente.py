import socket

def main():
    host = 'localhost'
    port = 13000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    request = "GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"
    client_socket.sendall(request.encode())

    response = client_socket.recv(4096).decode()
    print("Resposta do servidor:")
    print(response)

    client_socket.close()

if __name__ == "__main__":
    main()
