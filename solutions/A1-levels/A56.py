x1,y1,z1 = map(int,input().split())
x2,y2,z2 = map(int,input().split())

d = ( (x2-x1)** 2 + (y2-y1)**2 + (z2-z1)**2 )**(1/2)

print(f'{d:.2f}')
