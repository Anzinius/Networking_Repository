import httplib
import urllib

conn = httplib.HTTPConnection("github.com/anzinius")
#conn = httplib.HTTPConnection("github.com/anzinius", 80)
#conn = httplib.HTTPConnection("github.com/anzinius:80")

#conn.request("GET", "/ip")
conn.request("GET", "/get")
response = conn.getresponse()
data1 = response.read()
data2 = response.read().decode(“utf-8”)
print response.status
print response.reason
print data1
print data2

conn.close()