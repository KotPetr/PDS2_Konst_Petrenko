import socket

HOST = "127.0.0.1"
PORT = 12001

def messaging(client: socket.socket):
    message = input('Enter your message: ').encode('utf-8')
    client.send(message)
    data = client.recv(1024).decode('utf-8')
    print(f"Server: {str(data)}")


try:
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            try:
                client.connect((HOST, PORT))
                messaging(client)
            except ConnectionRefusedError:
                print('Server not responding.')


except KeyboardInterrupt as ex:
    print('\nServer connection terminated.')

except ConnectionResetError as ex:
    print(ex)

