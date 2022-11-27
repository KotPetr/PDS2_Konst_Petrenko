import logging
from dz_11_1_server import socket_server

server_logger = logging.getLogger('serverFL')
server_logger.setLevel(logging.INFO)

fh = logging.FileHandler(filename="server.log")

FORMAT = '%(asctime)s :: %(name)s :: %(lineno)s :: %(levelname)s :: %(message)s'
fh.setFormatter(logging.Formatter(FORMAT))

server_logger.addHandler(fh)
server_logger.info('Program started.')
socket_server()
server_logger.info("Program finished.\n")