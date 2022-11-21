import asyncio, socket

HOST = "127.0.0.1"
PORT = 12001

def add(str_list):
    return int(str_list[0]) + int(str_list[1])

def sub(str_list):
    return int(str_list[0]) - int(str_list[1])

def mult(str_list):
    return int(str_list[0]) * int(str_list[1])


async def run_server():
    with socket.create_server(('127.0.0.1', 12001)) as server:
        server.listen(5)
        print('Server is running...')
        while True:
            client_socket, address = server.accept()
            await asyncio.sleep(0)
            with client_socket:
                data = client_socket.recv(1024).decode('utf-8').split()
                print('Client: ', *data)
                try:
                    message = f'Sum of two numbers: {add(data)}, Difference of two numbers {mult(data)}, Multiplication of two numbers {sub(data)}'
                except Exception as ex:
                    message = 'Unknown input, please input two integer numbers.'

                print('Server: ',message)
                client_socket.send(message.encode('utf-8'))

try:
    asyncio.run(run_server())

except KeyboardInterrupt:
    print('\nServer has been stoped.')
except Exception as ex:
    print(ex)



