clist = {
    1:100,
    2:120,
    3:200,
    4:60
}
cal = 0

while True:
    n = int(input().strip())

    if n==5:break

    cal += clist[n]

print('Bye Bye')
print(f'Total Calories: {cal}')


