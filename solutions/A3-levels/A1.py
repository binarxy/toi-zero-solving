n = int(input())

ts = [None]*(n)
ans = 0

for i in range(0,n):
    ts[i] = list(map(int,input().split()))

#print(ts)

def recur(i):
    global ans
    a,l,b,r = ts[i-1]
    
    if a==1:
        left = l
    else:
        left = recur(l)

    if b==1:
        right = r
    else:
        right = recur(r)

    if left < right :
        ans += (right-left)
        left = right
    elif right < left:
        ans += (left-right)
        right = left

    return left + right

recur(1)
print(int(ans))

