m,n = map(int,input().strip().split())
pn = int(input())

maps = [ [0] * n for _ in range(m) ]

directions = {
    (-1,-1),(-1,0),(-1,1),
    (0,-1),       (0,1),
    (1,-1),(1,0),(1,1)
}

max_pk = 0

for _ in range(pn):
    x,y = map(int,input().strip().split())
    maps[x][y] += 1

for i in range(m):
    for j in range(n):
        if maps[i][j] == 0:
            count = 0

            for dx,dy in directions:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < m and 0 <= nj < n:
                    if maps[ni][nj] >= 1:
                        count += maps[ni][nj]

            
            max_pk = max(max_pk,count)

print(max_pk)
