#from hfunc.log import alog2d

n,m = map(int,input().split())
maps = [ [0]*m for _ in range(n)]

bx,by = map(int,input().split())

risk = 0

directions = {
    (-2,-2),(-2,-1),(-2,0),(-2,1),(-2,2),
    (-1,-2),(-1,-1),(-1,0),(-1,1),(-1,2),
    (0,-2),(0,-1),        (0,1),(0,2),
    (1,-2),(1,-1), (1,0), (1,1),(1,2),
    (2,-2),(2,-1),(2,0),(2,1),(2,2)
}

for _ in range(int(input().strip())):
    y,x = map(int,input().split())

    maps[y][x] = 10

    for dy,dx in directions:
        ny = y + dy
        nx = x + dx

        if 0 <= ny < n and 0 <= nx < m:
            if (abs(dy) == 2 or abs(dx) == 2):
                risk = 2
            else:
                risk = 6
            
            maps[ny][nx] = max(maps[ny][nx],risk)


count = sum(num==0 for row in maps for num in row)

# alog2d(maps)

print(count)
print(f'{maps[bx][by]*10}%')