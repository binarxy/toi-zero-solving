n = int(input())
nums = list(map(int,input().strip().split()))

sum = 0
even = 0
odd = 0

for num in nums:
    if abs(num) % 2 == 0:
        even += 1
    else:
        odd += 1

    sum += num

print(f'SUM {sum}')
print(f'EVEN {even}')
print(f'ODD {odd}')