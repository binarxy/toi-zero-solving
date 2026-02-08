firstname = input().strip()
lastname = input().strip()
age = input().strip()

if len(firstname) > 5 and len(lastname) > 5:
    print(f'{firstname[:2]}{lastname[-1]}{age[-1]}')
else:
    print(f'{firstname[0]}{age}{lastname[-1]}')