a = int(input())
b = int(input())
d = int(input())
r = int(input())

xf = a + ((r-a) % d)

if xf>b: print(0)
else:
    print((b-xf) // d+1)
