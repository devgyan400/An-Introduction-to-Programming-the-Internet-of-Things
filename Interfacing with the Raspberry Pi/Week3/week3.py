import http.client

conn = http.client.HTTPSConnection("www.uci.edu")
conn.request("GET", "/")
rsp = conn.getresponse()
print(rsp.status, rsp.reason)

content=resp.read(1000)
print(content)
conn.close()
