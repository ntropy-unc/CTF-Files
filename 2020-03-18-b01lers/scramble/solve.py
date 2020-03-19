words = []
ans = [None] * 68
ans[0] = "pc"

with open('log') as f:
    for l in f.readlines():
        l = l.strip('\n')
        l = l.split('kxkxkxkxsh')
        words.append(l[1])

for w in words:
    offset = -1
    for x in range(len(w)):
        if not w[-(x+1):].isnumeric():
            offset = -x
            break
    ans[int(w[offset:])] = w[:offset]

import urllib.parse
print(''.join([urllib.parse.unquote(a)[:-1] for a in ans]))
