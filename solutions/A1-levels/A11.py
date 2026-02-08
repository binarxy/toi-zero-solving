s = input().strip()
counter = {}

for ch in s:
    if ch in counter:
        counter[ch] += 1
    else:
        counter[ch] = 1

for key,value in counter.items():
    print(f'{value}{key}',end='')