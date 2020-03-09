from pwn import *
import string
import time

context.log_level = 'error'
host = 'crypto.utctf.live'
port = '9004'

guess = 'utflag{000000000000000000000000}'

for x in range(24):
    for s in string.printable:
        r = remote(host, port)
        data = r.recvline()
        flag = data.decode('utf-8').split(' ')[1].strip('\n')
        r.recv(4096)
        guess = guess[:7 + x] + s + guess[8 + x:]
        r.sendline(b'1')
        r.sendline(guess)
        cipher_guess = r.recvlines(9)
        cipher_guess = cipher_guess[2].decode('utf-8').split(',')[0][2:-1]
        if cipher_guess[:(8 + x) * 2] == flag[:(8 + x) * 2]:
            print(guess)
            break
        r.close()
    print('guess one letter?')