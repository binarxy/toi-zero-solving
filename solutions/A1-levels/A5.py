month = int(input().strip())
days = int(input().strip())

if days >= 21:
    month += 1

if month <= 3 or month == 13:
    print('winter')
elif month <= 6:
    print('spring')
elif month <= 9:
    print('summer')
elif month <= 12:
    print('fall')
