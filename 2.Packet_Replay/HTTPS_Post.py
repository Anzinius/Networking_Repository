import httplib
import urllib

conn = httplib.HTTPSConnection("github.com/anzinius")

params = "test data"
headers = {"Connection" : "Keep-Alive",
    "Host" : "192.168.0.0",
    "User-Agent" : ""
}
conn.request("POST", "/post", params, headers)
response = conn.getresponse()
data = response.read()
print response.status
print response.reason
print data

conn.close()