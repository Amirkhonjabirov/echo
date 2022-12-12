HOST = '127.0.0.1'
PORT = 9999

requests_data = [
    {
        'method': 'GET',
        'path': '/',
        'protocol_version': 'HTTP/1.1',
        'host': f'{HOST}:{PORT}',
        'headers':
            {
                'Accept-Language': 'fr',
            },
    },
    {
        'method': 'GET',
        'path': '/?status=404',
        'protocol_version': 'HTTP/1.1',
        'host': f'{HOST}:{PORT}',
        'headers':
            {
                'Accept-Language': 'fr',
            },
    },
    {
        'method': 'POST',
        'path': '/?status=200',
        'protocol_version': 'HTTP/1.1',
        'host': f'{HOST}:{PORT}',
        'headers':
            {
                'Accept-Language': 'RU_ru',
            },
    },
    {
        'method': 'POST',
        'path': '/?status=500',
        'protocol_version': 'HTTP/1.1',
        'host': f'{HOST}:{PORT}',
        'headers':
            {
                'Accept-Language': 'RU_ru',
            },
    },
    {
        'method': 'POST',
        'path': '/?status=50',
        'protocol_version': 'HTTP/1.1',
        'host': f'{HOST}:{PORT}',
        'headers':
            {
                'Accept-Language': 'RU_ru',
            },
    },
    {
        'method': 'GET',
        'path': '/?status=200',
        'protocol_version': 'HTTP/1.1',
        'host': f'{HOST}:{PORT}',
        'headers': {
            'User-Agent': 'PostmanRuntime/7.29.2',
            'Accept': '*/*',
            'Postman-Token': 'd2690a27-ace7-4271-8e93-f1702a13d38a',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        },
    },
    {
        'method': 'PUT',
        'path': '/?status=304',
        'protocol_version': 'HTTP/1.1',
        'host': f'{HOST}:{PORT}',
        'headers': {
            'User-Agent': 'PostmanRuntime/7.29.2',
            'Accept': '*/*',
            'Postman-Token': 'd2690a27-ace7-4271-8e93-f1702a13d38a',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        },
    },
]
