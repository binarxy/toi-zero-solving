n=int(input())

print(f'10 = {int(n//10)}')
n-=(n//10) * 10

print(f'5 = {int(n//5)}')
n-=(n//5) * 5

print(f'2 = {int(n//2)}')
n-=(n//2) * 2

print(f'1 = {int(n//1)}')
