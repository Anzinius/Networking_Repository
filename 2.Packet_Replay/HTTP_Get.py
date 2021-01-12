import httplib
import urllib

conn = httplib.HTTPConnection("github.com/anzinius")

#conn.request("GET", "/ip")
conn.request("GET", "/get")
response = conn.getresponse()
data = response.read()
print response.status
print response.reason
print data

conn.close()