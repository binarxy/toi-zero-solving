n = int(input().strip())
ch1 = input().strip().split()
ch2 = input().strip().split()

count = 0
pairs = {
    'A':'T',
    'T':'A',
    'C':'G',
    'G':'C',
}

for _ in range(int(input().strip())):
    line,pos,base = input().split()

    if line == '1':
        ch1[int(pos)] = base
    elif line == '2':
        ch2[int(pos)] = base

for i in range(n):
    if pairs[ch1[i]] != ch2[i]: count += 1

print(' '.join(ch1))
print(' '.join(ch2))
print(count)