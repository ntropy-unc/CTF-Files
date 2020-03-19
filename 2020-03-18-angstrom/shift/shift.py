def f(nth):
  sq5 = 5**.5
  phi1 = (1+sq5)/2
  phi2 = -1 * (phi1 -1)
  resp = (phi1**(nth+1) - phi2**(nth+1))/sq5
  return int(resp)

def rot(s, n):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join([upper[(upper.find(a)+n) % 26] for a in s])

from pwn import *

context.log_level = 'error'

r = remote('misc.2020.chall.actf.co', '20300')
r.recvuntil('--------------------\n')
for x in range(50):
    data = r.recvline()
    print(data)
    data = data.decode().strip('\n').split(' ')
    print(data)
    cipher, fibon = data[1], f(int(data[3].replace('n=', '')) - 1)
    ans = rot(cipher, fibon % 26)
    print(ans)
    r.recvuntil(': ')
    r.sendline(ans)
print(r.recv(4096))