age,day = map(str,input().split())
price = 0

if int(age) >= 19:
    price = 150
elif int(age) >=5:
    price = 100

if day == 'Wed':
    price /= 2

print(int(price))