import socket

HOST = "127.0.0.1"
PORT = 12001

try:
    with socket.create_server(('127.0.0.1', 12001)) as server:
        server.listen(5)
        print('Server is running...')

        while True:
            client_socket, addr = server.accept()
            with client_socket:
                data = client_socket.recv(1024).decode('utf-8')
                print('Client: ', data)
                while True:
                    message = input('Enter your message: ')
                    if len(message) > 0:
                        break
                client_socket.send(message.encode('utf-8'))

except KeyboardInterrupt:
    print('\nServer has been stoped.')
except Exception as ex:
    print(ex)

