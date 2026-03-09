mA = [ list(map(int,input().split())) for _ in range(3)]
mB = [ list(map(int,input().split())) for _ in range(3)]

ans = []

for i in range(3):
    row = []
    for j in range(3):
        s = (mA[i][0]*mB[0][j]) + (mA[i][1]*mB[1][j]) + (mA[i][2]*mB[2][j])
        row.append(s % (2**15+9))
    ans.append(row)

for row in ans:
    print(' '.join(map(str,row)))

