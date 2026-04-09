a,b,d,r = map(int,input().split())

n=0
for i in range(a,b+1):
    if i%d == r : n+=1

print(n)
