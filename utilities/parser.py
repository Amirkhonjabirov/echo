from http import HTTPStatus
from datetime import datetime
from re import match


def parse_data(string: str):
    _data = [x for x in string.split('\r\n') if x != '']
    method_template = '(?P<method_type>[A-Z]+) (?P<path>[/?=a-z0-9.:]*) (?P<protocol_version>[A-Z/.0-9]*)'
    method_info_match_res = match(method_template, _data[0])

    phrase = ''
    try:
        status_code = method_info_match_res.group('path')[-3:]
        for item in list(HTTPStatus):
            if item.value == int(status_code):
                phrase = item.phrase
        if phrase == '':
            raise Exception

    except Exception:
        status_code = '200'
        phrase = 'OK'

    method_info = {
        'method_type': method_info_match_res.group('method_type'),
        'path': method_info_match_res.group('path'),
        'protocol_version': method_info_match_res.group('protocol_version'),
        'status_code': status_code,
        'status_phrase': phrase,
    }

    request_source_template = 'Host: (?P<ip>.*?):(?P<port>[0-9]*)'
    request_source_match_res = match(request_source_template, _data[1])
    host_info = f'({request_source_match_res.group("ip")}:{request_source_match_res.group("port")})'

    headers = _data[2:]
    headers_dict = {}
    for header in headers:
        header = header.split(':')
        headers_dict[header[0]] = header[1]
    return method_info, host_info, headers_dict


def make_result_str_for_sending(method_info: dict, host_info: str, headers: dict):
    server_time_now = datetime.now()
    res_str = (
        f'Request time:{server_time_now}\r\n'
        f'Request Method:{method_info["method_type"]}\r\n'
        f'Response Status:{method_info["status_code"]} {method_info["status_phrase"]}\n'
        f'Request Source:{host_info}\r\n'
    )
    for key, value in headers.items():
        res_str += f'{key}:{value}\r\n'
    return res_str
