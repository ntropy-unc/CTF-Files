import requests

base = 'http://web.ctf.b01lers.com:1002/'
transmissions = set()

s = requests.Session()

for x in range(1000):
    resp = s.get(base)
    if x == 0: # Ignore 0 cookie
        continue
    t = s.cookies.get_dict()['transmissions']
    transmissions.add(t)

for t in transmissions:
    print(t)
