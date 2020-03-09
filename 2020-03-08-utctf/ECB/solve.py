from pwn import *
from binascii import unhexlify
import string
import os

context.log_level = 'error'
host, port = 'ecb.utctf.live', '9003'

r = remote(host, port)

def oracle(salt=''):
    while True:
        try:
            ans = set()
            while len(ans) != 2:
                r.recv(4096)
                r.sendline(salt)
                r.recvline()
                data = r.recvline().decode().strip('\n')
                ans.add(unhexlify(data))
            return ans
        except:
            continue

def offset():
    slen = len(max(oracle(salt='a' * 1), key=lambda a:len(a)))
    for x in range(1, 32):
        newlen = len(max(oracle(salt='a' * x), key=lambda a:len(a)))
        if newlen > slen:
            print(x)
            return newlen - slen

def same_block(data):
    m = set()
    for x in range(0, len(data), 16):
        t = data[x:x + 16]
        if t in m:
            return True
        m.add(t)
    return False

def exploit():
    plain = b''
    for b in range(2):
        block = b''
        for x in range(15, -1, -1):
            if b == 0:
                pad = b'X' * x
            elif x == 0:
                pad = b''
            else:
                pad = plain[-x:]
            for word in string.printable:
                stop = False
                word = word.encode('utf-8')
                if word == b'A': continue
                exploit = pad + block + word + b'X' * x
                data = oracle(salt=exploit)
                for i, d in enumerate(data):
                    if word == b'~':
                        print(len(d))
                    if same_block(d):
                        block += word
                        print(block)
                        stop = True
                        break
                if stop:
                    break
            print('Moved on')
        plain += block

    print(plain)

# print(offset())
exploit()