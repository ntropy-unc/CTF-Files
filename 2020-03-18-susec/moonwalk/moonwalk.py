x = 121
guess = chr(x)
guess += chr(ord(guess[-1]) ^ 0x49)
guess += chr(ord(guess[-1]) ^ 0x45)
guess += chr(ord(guess[-1]) ^ 0x2a)
guess += chr(ord(guess[-1]) ^ 0x28)
guess += chr(ord(guess[-1]) ^ 0x46)
guess += chr(ord(guess[-1]) ^ 0x5d)
guess += chr(ord(guess[-1]) ^ 0x10)
guess += chr(ord(guess[-1]) ^ 0x23)

sus = [0x70, 0x77, 0x6e, 0x34, 0x77, 0x6c, 0x69, 0x6b, 0x37, 0x5f, 0x65, 0x77, 0x76, 0x68, 0x6e, 0x33, 0x75, 0x6e, 0x62, 0x5f, 0x37, 0x31, 0x30, 0x74]

guess += ''.join([chr(s) for i, s in enumerate(sus) if i % 2 == 1])

from binascii import unhexlify
ans = 0x20c44eba3078d09c ^ 0x45a9278d6f0be1c3
guess += unhexlify(hex(ans)[2:]).decode('utf-8')[::-1]
guess += '_'

guess += '?' * (0x29 - len(guess))
print("SUSEC{" + guess + "}")
