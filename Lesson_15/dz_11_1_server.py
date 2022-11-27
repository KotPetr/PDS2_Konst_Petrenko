import logging
import socket

def socket_server(host = '127.0.0.1', port = 12001):
    server_logger = logging.getLogger('serverFL')
    server_logger.info(f"Setting host: {host} and port: {port}")
    try:
        with socket.create_server((host, port)) as server:
            server.listen(5)
            print('Server is running...')
            server_logger.info(f'Server is running on {host}:{port}')

            while True:
                client_socket, addr = server.accept()
                server_logger.info('Client connected. Waiting for message.')
                with client_socket:
                    data = client_socket.recv(1024).decode('utf-8')
                    print('Client: ', data)
                    server_logger.info('Message from client has been recived.')
                    while True:
                        message = input('Enter your message: ')
                        if len(message) > 0:
                            break
                        else:
                            server_logger.warning('Message can not be empty!')
                    client_socket.send(message.encode('utf-8'))
                    server_logger.info(f'Message to the client has been send.')

    except KeyboardInterrupt:
        print('\nServer has been stoped.')
        server_logger.error("Server has been stoped.")
    except Exception as ex:
        print(ex)
        server_logger.error(ex)
    finally:
        server_logger.info("Done!")














