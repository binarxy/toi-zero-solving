n = int(input())

if n < 100 or n % 100 != 0 or n>20000:
    print("ERROR")
else:
    if n>=1000:
        print(f'1000 = {int(n)//1000}')
        n -= 1000 * (n//1000)
    if n>=500:
        print(f'500 = {int(n)//500}')
        n -= 500 * (n//500)
    if n>=100:
        print(f'100 = {int(n)//100}')
        n -= 100 * (n//100)


