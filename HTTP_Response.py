from urllib.request import urlopen
from urllib.error import URLError, HTTPError

code = str()
f = open("http_status_code.txt", "w")

url = ["https://github.com/Anzinius", "https://github.com/Anzinius/Network", "https://github.com/Anzinius/Networking_Repository"]

def readStatusCode(url):
    try:
        response = urlopen(url)
        code = response.status
    except HTTPError as e:
        error = e.read()
        code = e

def writeStatusCode(code):
    f.write(code)

for u in url:
    readStatusCode(u)
    writeStatusCode(code)

f.close()