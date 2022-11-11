import socket

HOST = "127.0.0.1"
PORT = 12001

def chat_bot(mes, addr):
    mes = mes.lower().strip().replace('.', '')
    chat_bot_dict = {'привіт': 'Доброго дня.', 'як справи?': 'Відмінно!', 'яка у тебе адреса?': f'IP aдреса, порт: {addr}', 'пока': 'На все добре.'}
    phrases = ", ".join([str(x).capitalize() for x in chat_bot_dict.keys()])
    return chat_bot_dict.get(mes.lower()) if mes in chat_bot_dict.keys() \
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
                message = chat_bot(data, address).encode('utf-8')
                client_socket.send(message)

except KeyboardInterrupt:
    print('\nServer has been stoped.')