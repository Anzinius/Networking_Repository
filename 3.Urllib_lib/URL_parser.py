from urllib.parse import urlparse
from urllib.parse import urlsplit

parsedURL = urlparse('https://github.com/Anzinius/Networking_Repository/blob/main/3.Urllib_lib/URL_parser.py')
print(parsedURL)
print(parsedURL.scheme)
print(parsedURL.port)

splitedURL = urlsplit('https://github.com/Anzinius/Networking_Repository/blob/main/3.Urllib_lib/URL_parser.py')
print(splitedURL)