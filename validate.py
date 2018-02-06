import re
from datetime import datetime
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


LINE_PATTERN = re.compile(
                r"(?P<ip>[\d.]+)\s+"  # IP address
                r"\[(?P<dt>[\w\s+-:]+)\]\s+"  # datetime string
                r"\"(?P<method>[A-Z]+)\s+"  # request method
                r"(?P<url>[\w\-._~:/?#\[\]@!$&'()*+,;=`]+)\s+"  # URL
                r"HTTP/\d\.\d+\"\s+"  # version
                r"(?P<code>\d+)\s+"  # response code
                r"\d+\s*"  # bytes sent
                )
IPv4_PATTERN = re.compile(r"^(?:(?:\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(?:\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$")
# 4 integers in range 0-255 separated by dots

REQUEST_PATTERN = re.compile(r"^(?:GET|HEAD|POST|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH)$")
# one of possible request methods

RESPONSE_PATTERN = re.compile(r"^[2-5]\d\d$")  # 3 digit code, with first digit equal to 2, 3, 4 or 5
VAL = URLValidator()


def _is_valid_ipv4(ip_address):
    return True if IPv4_PATTERN.search(ip_address) else False


def _is_valid_datetime(dt):
    try:
        datetime.strptime(dt, '%d/%b/%Y:%H:%M:%S %z')
    except ValueError:
        return False
    return True


def _is_valid_request_method(method):
    return True if REQUEST_PATTERN.search(method) else False


def _is_valid_url(url):
    try:
        VAL(url)
    except ValidationError:
        return False
    return True


def _is_valid_response(code):
    return True if RESPONSE_PATTERN.search(code) else False


def is_valid_line(line):
    """
    Validate line of log file
    :param str line: line of log file
    :return: bool: True if line is valid, False if not
    """
    m = LINE_PATTERN.search(line)
    if not m:
        return False
    ip = m.group('ip')
    dt = m.group('dt')
    request_method = m.group('method')
    url = m.group('url')
    response_code = m.group('code')
    if _is_valid_ipv4(ip) and _is_valid_datetime(dt) and _is_valid_request_method(request_method) \
            and _is_valid_url(url) and _is_valid_response(response_code):
        return True
    return False
