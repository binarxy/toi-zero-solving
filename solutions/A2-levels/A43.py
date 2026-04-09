size=int(input())
maps=input().split()
mp=input()

pos=maps.index('1')

s={'L':-1,'R':1}

for move in mp:
    if (move == 'L' and pos<=0) or (move == 'R' and pos>=size-1):
        continue

    if maps[pos+s[move]] == '2':
        maps[pos] = '0'
        maps[pos+s[move]] = '1'
        break

    maps[pos] = '0'
    maps[pos+s[move]] = '1'
    pos+=s[move]

print(' '.join(maps))
