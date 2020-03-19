from pwn import *
context.log_level = 'error'
import random
from sympy import *

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m

def tetration(a, x, p):
    tot = reduced_totient(p)
    if tot == 1 or x == 0:
        return 1
    else:
        return pow(a, tetration(a, x - 1, tot), p)

# x = ?
# a ^^ x = b mod p
def brute():
    r = remote('3.228.7.55', '20603')
    banner = r.recvlines(3)
    for _ in range(10):
        print(f"{_ + 1}/10")
        data = r.recvlines(3)
        p = int(data[0].decode().split(' ')[2])
        a = int(data[1].decode().split(' ')[2])
        b = int(data[2].decode().split(' ')[2])
        enter = r.recv(4096)
        print(f"p= {p}")
        print(f"a= {a}")
        print(f"b= {b}")
        if a == b:
            r.sendline(str(1))
        else:
            skip = False
            x = 1
            while x < reduced_totient(p):
                data = tetration(a, x, p)
                if data == b:
                    r.sendline(str(x))
                    print(f"find, ans was {str(x)}")
                    skip = True
                    break
                x += 1
            if not skip:
                r.sendline(str(p - 1))
                print('didnt find')
        resp = r.recvline()
        if resp.decode().find('Wrong') != -1:
            break
        else:
            print(r.recvline())
            if _ == 9:
                print(resp)
                r.interactive()
                dontstop = True
                break

brute()