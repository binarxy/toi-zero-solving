m,n = map(int,input().split())
rd,md,fd = map(int,input().split())

points = {'r' : 0,'m' : 0,'f' : 0}

for _ in range(n):
    pos,score = map(int,input().split())
    if pos > m:
        continue

    if pos % rd == 0:
        points['r'] += score
    if pos % md == 0:
        points['m'] += score
    if pos % fd == 0:
        points['f'] += score

m_score = max(points['r'],points['m'],points['f'])

if points['r'] == m_score:
    print('Rabbit',m_score)
if points['m'] == m_score:
    print('Monkey',m_score)
if points['f'] == m_score:
    print('Frog',m_score)

