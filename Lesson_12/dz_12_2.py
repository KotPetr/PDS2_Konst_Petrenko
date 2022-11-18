import asyncio, socket

HOST = "127.0.0.1"
PORT = 12001

async def add(str_list):
    return int(ls[0]) * int(ls[1])

async def sub(str_list):
    return int(ls[0]) * int(ls[1])

async def mult(str_list):
    return int(ls[0]) * int(ls[1])


try:
    with socket.create_server(('127.0.0.1', 12001)) as server:
        server.listen(5)
        print('Server is running...')
        while True:
            client_socket, address = server.accept()
            with client_socket:
                data = client_socket.recv(1024).decode('utf-8').split()
                print('Client: ', *data)
                result = process_numbers(data)
                message = f'Sum of two numbers: {result[0]}, Difference of two numbers {result[1]}, Multiplication of two numbers {result[2]}'
                print('Server: ',message)
                client_socket.send(f'There are {message} words in your phrase'.encode('utf-8'))

except KeyboardInterrupt:
    print('\nServer has been stoped.')



async def handle_client(client):
    loop = asyncio.get_event_loop()
    request = None
    while request != 'quit':
        request = (await loop.sock_recv(client, 255)).decode('utf8')
        response = str(eval(request)) + '\n'
        await loop.sock_sendall(client, response.encode('utf8'))
    client.close()


async def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 15555))
    server.listen(8)
    server.setblocking(False)

    loop = asyncio.get_event_loop()

    while True:
        client, _ = await loop.sock_accept(server)
        loop.create_task(handle_client(client))

asyncio.run(run_server())