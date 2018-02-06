import sys
import re
import csv
from validate import is_valid_line


def strip_url(line):
    """
    Strip URL from line in log file ignoring the protocol,
    ending slash and query string parameters
    :param str line: line of log file
    :return: str stripped url
    """
    url_without_protocol = re.search(r'[A-Z]+\shttps?://(?P<url>.*\s)[A-Z]+', line).group('url')
    stripped_url = re.split(r'/?(\?.*)?\s', url_without_protocol)[0]
    return stripped_url


def process_log_file(file):
    """
    Count requests for each of valid URLs and count invalid lines
    :param str file: log file path
    :return: (dict url_request_count: number of requests for each valid URL,
    int invalid_lines: number of invalid lines in log file)
    """
    invalid_lines = 0
    url_request_count = {}
    with open(file, encoding='utf-8') as f:
        for line in f:
            if not is_valid_line(line):
                invalid_lines += 1
                continue
            url = strip_url(line)
            if url in url_request_count:
                url_request_count[url] += 1
            else:
                url_request_count[url] = 1
    return url_request_count, invalid_lines


def write_to_stdout(sorted_requests):
    """
    Write generated report to standard output
    :param list sorted_requests: sorted list of tuples in form: (URL, number of requests)
    :return: None
    """
    writer = csv.writer(sys.stdout)
    for item in sorted_requests:
        writer.writerow(item)


def sort_url(url_count):
    """
    Sort the records in the result, firstly by the number of requests in descending order,
    and if two URLs are requested equally often, sort them lexicographically.
    :param dict url_count: number of requests for each valid URL
    :return: sorted list of tuples in form: (URL, number of requests)
    """
    return sorted(url_count.items(), key=lambda x: (-x[1], x[0]))


def write_to_stderr(invalid_lines):
    """
    Write number of invalid log lines to standard error
    :param int invalid_lines: number of invalid lines
    :return: None
    """
    if invalid_lines:
        sys.stderr.write('Invalid log lines: %d\n' % invalid_lines)


def main():
    log_file = sys.argv[1]
    url_request_count, invalid_lines = process_log_file(log_file)
    sorted_requests = sort_url(url_request_count)
    write_to_stdout(sorted_requests)
    write_to_stderr(invalid_lines)


if __name__ == "__main__":
    main()
