import socket
from random import choice

from utilities.settings import HOST, PORT, requests_data


def get_random_data_for_request():
    _request_data = choice(requests_data)
    result = f'{_request_data["method"]} {_request_data["path"]} {_request_data["protocol_version"]}\r\n' \
             f'Host: {_request_data["host"]}\r\n'
    for key, value in _request_data['headers'].items():
        result += f'{key}: {value}\r\n'
    result += '\r\n'
    return result


end_of_stream = '\r\n\r\n'

with socket.socket() as client_socket:
    client_socket.connect((HOST, PORT))

    request_data = get_random_data_for_request()
    client_socket.send(request_data.encode())

    client_data = ''
    while True:
        data = client_socket.recv(1024)
        print('Received: \n', data.decode('utf-8'))
        if not data:
            break
        client_data += data.decode()
        if end_of_stream in client_data:
            break
