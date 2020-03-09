c1 = "3b3b463829225b3632630b542623767f39674431343b353435412223243b7f162028397a103e"
c2 = "213c234c2322282057730b32492e720b35732b2124553d354c22352224237f1826283d7b0651"

cribs = ["Cryptography", "Networking", "Reverse Engineering", "Binary Exploitation", "Web", "Forensics", "Misc"]

def xor_strings(xs, ys, offset=0):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys[offset:]))

twotime = xor_strings(c1.decode('hex'), c2.decode('hex'))

'''
for x in cribs:
    print(x)
    print("===================")
    for y in range(0, len(twotime) - len(x)):
        print(xor_strings(x, twotime, offset=y))
'''

plaintext = 'NO THE BEST ONE IS BINARY EXPLOITATION'
print(xor_strings(c1.decode('hex'), plaintext))
print(xor_strings(c2.decode('hex'), plaintext))