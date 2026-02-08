even = 0
odd = 0

for _ in range(3):
    n = int(input().strip())

    if n % 2 == 0: even += 1
    else: odd += 1

print(f'even {even}')
print(f'odd {odd}')

