import requests

def ip(url="http://ifconfig.cc"):
    r = requests.get(url)
    return r.text

val = ip()
print(val)