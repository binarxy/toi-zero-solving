n,q = map(int,input().split())

r = []
ans = []

for _ in range(n):
    s,t = map(int,input().split())
    r.append((s,t))

query = input().split()

for i in query:
    count = 0
    for j in r:
        if int(i) >= j[0] and int(i) <= j[1]:
            count += 1
    ans.append(str(count))

print(' '.join(ans))
