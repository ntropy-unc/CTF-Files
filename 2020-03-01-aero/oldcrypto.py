from pwn import *
import re
from base64 import b64decode

context.log_level = 'error' # Disable non error related messages
host, port = 'tasks.aeroctf.com', '44323'

def oracle(salt=''):
    while True:
        try:
            r = remote(host, port)
            r.recv(4096)
            r.sendline('3')
            r.recv(4096)
            r.sendline(salt)
            data = r.recv(4096).decode()
            b64 = data.split("'")[1]
            return b64decode(b64.encode())
        except:
            continue
        break

def offset():
    compare = len(oracle())
    for x in range(1, 16):
        if len(oracle(salt='a' * x)) != compare:
            return x

offset = 16 - 10 # As expected because AERO{32} => (6 + 32) % 16
word_bank = ['A', 'a', 'b', 'c', 'd', 'e', 'f', 'r', 'o', '{', '}',
             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\x00']

def same_block(data):
    m = set()
    for x in range(0, len(data), 16):
        t = data[x:x + 16]
        if t in m:
            return True
        m.add(t)
    return False

plain = ''
for b in range(3):
    block = ''
    for x in range(15, -1, -1):
        if b == 0:
            pad = 'a' * x
        elif x == 0:
            pad = ''
        else:
            pad = plain[-x:]
        for word in word_bank:
            exploit = pad + block + word + 'a' * x
            data = oracle(salt=exploit)
            if same_block(data):
                block += word
                break
    plain += block

print(plain)
