import httplib
import urllib

conn = httplib.HTTPSConnection("github.com/anzinius")
#conn = httplib.HTTPConnection("github.com/anzinius", 443)
#conn = httplib.HTTPConnection("github.com/anzinius:443")

#conn.request("GET", "/ip")
conn.request("GET", "/get")
response = conn.getresponse()
data = response.read()
print(response.status)
print(response.reason)
print(data)

conn.close()