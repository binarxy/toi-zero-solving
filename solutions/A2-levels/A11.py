n=input().strip()
nd = []

for num in n.split():
    if not num in nd:
        nd.append(num)

print(' '.join(nd))
