from urllib.request import urlopen
from urllib.error import URLError, HTTPError

url = "https://github.com/Anzinius"
try:
    response = urlopen(url)
    print(response.status)
except HTTPError as e:
    error = e.read()
    code = e.getcode()
    print(code)

