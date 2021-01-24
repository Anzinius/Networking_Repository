import httplib
import urllib

conn = httplib.HTTPConnection("github.com/anzinius")
#conn = httplib.HTTPConnection("github.com/anzinius", 80)
#conn = httplib.HTTPConnection("github.com/anzinius:80")

params = "test data"
headers = {"Connection" : "Keep-Alive",
    "Host" : "192.168.0.0",
    "User-Agent" : ""
}
conn.request("POST", "/post", params, headers)
response = conn.getresponse()
data = response.read()
print(response.status)
print(response.reason)
print(data)

conn.close()