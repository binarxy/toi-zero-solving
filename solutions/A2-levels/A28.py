n=int(input())
s1=input().strip()
s2=input().strip()

count = 0

for i in range(n):
    if int(s1[i]) + int(s2[i]) != 9:
        count += 1

if count:
    print(f'NO {count}')
else:
    print('YES')


