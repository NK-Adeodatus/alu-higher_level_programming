#!/usr/bin/python3
""" script that takes in a URL and an email,
sends a POST request to the passed URL with
the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""


if __name__ == '__main__':
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    import sys
    data = urlencode({"email": sys.argv[2]
                      }).encode("ascii")

    request = Request(sys.argv[1], data)
    with urlopen(request) as response:
        print(response.read().decode('utf-8'))
