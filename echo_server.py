import socket
from datetime import datetime

from utilities.parser import make_result_str_for_sending, parse_data
from utilities.settings import HOST, PORT

end_of_stream = '\r\n\r\n'


def handle_client(connection):
    client_data = ''
    with connection:
        while True:
            data = connection.recv(1024)
            print('Received: \n', data.decode('utf-8'))
            if not data:
                break
            client_data += data.decode()
            if end_of_stream in client_data:
                break

        method_info, host_info, headers = parse_data(data.decode('utf-8'))

        http_response = (
            f"{method_info['protocol_version']} {method_info['status_code']} {method_info['status_phrase']}\r\n"
            f"Server: {host_info}\r\n"
            f"Date: {datetime.now()}\r\n"
            f"Content-Type: text/html; charset=UTF-8\r\n"
            f"\r\n"
        )
        result_str = make_result_str_for_sending(method_info=method_info, host_info=host_info, headers=headers)
        connection.send(http_response.encode() + result_str.encode() + f"\r\n".encode())


with socket.socket() as serverSocket:
    serverSocket.bind((HOST, PORT))
    serverSocket.listen()

    while True:
        (clientConnection, clientAddress) = serverSocket.accept()
        handle_client(clientConnection)
        print(f'Sent data to {clientAddress}')
