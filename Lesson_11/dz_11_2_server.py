import socket

HOST = "127.0.0.1"
PORT = 12001

def chat_bot(mess, addr):
    mess = mess.lower().strip().replace('.', '')
    chat_bot_dict = {'привіт': 'Доброго дня.', 'як справи?': 'Відмінно!', 'твоя адреса?': f'IP aдреса, порт: {addr}', 'пока': 'На все добре.'}
    phrases = "; ".join([str(x).capitalize() for x in chat_bot_dict.keys()]) + ' (перериває сеанс)'
    return chat_bot_dict.get(mess.lower()) if mess in chat_bot_dict.keys() \
        else 'Вибачте, я вас на зрозумів.\nСписок доступних фраз: ' + phrases


try:
    with socket.create_server(('127.0.0.1', 12001)) as server:
        server.listen(5)
        print('Server is running...')
        while True:
            client_socket, address = server.accept()
            with client_socket:
                data = client_socket.recv(1024).decode('utf-8')
                print('Client: ', data)
                message = chat_bot(data, address)
                print('Server: ',message)
                client_socket.send(message.encode('utf-8'))
                if data.lower() == 'пока':
                    print('Connection terminated.')
                    break

except KeyboardInterrupt:
    print('\nServer has been stoped.')