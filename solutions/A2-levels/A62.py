s = input().strip().lower()
d = {'a':0,'e':0,'i':0,'o':0,'u':0}

for ch in s:
    if ch in d:
        d[ch] += 1

for k,v in d.items():
    if v == 0: continue
    print(f'{k}: {v}')
