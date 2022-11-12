import socket

HOST = "127.0.0.1"
PORT = 12001

def words_quantity(string: str):
    str_list = string.split()
    count = 0
    for word in str_list:
        count +=1 if word not in '-,!?.;:()[]\\/"''' else 0
    return count


try:
    with socket.create_server(('127.0.0.1', 12001)) as server:
        server.listen(5)
        print('Server is running...')
        while True:
            client_socket, address = server.accept()
            with client_socket:
                data = client_socket.recv(1024).decode('utf-8')
                print('Client: ', data)
                message = words_quantity(data)
                print('Server: ',message)
                client_socket.send(f'There are {message} words in your phrase'.encode('utf-8'))

except KeyboardInterrupt:
    print('\nServer has been stoped.')