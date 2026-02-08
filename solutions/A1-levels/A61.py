r,x,y = map(int,input().strip().split())

d = ( x**2 + y ** 2)**(1/2)

if d**2 < r**2:
    print('IN')
elif d**2 == r**2:
    print('ON')
elif d**2 > r**2:
    print('OUT')