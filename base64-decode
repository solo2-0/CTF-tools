import base64

c = open("Flag.txt","r")// input base64 file
f = open("sample.txt","wb") // output decoded file
a = c.read()
a.lstrip()
a.strip()
a.rstrip()
print a
b = base64.decodestring(a)
f.write(b)
