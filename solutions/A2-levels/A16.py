lot,mylot = input(),input()

if lot == mylot:
    print('1000000')
elif lot[2:7] == mylot[2:7]:
    print('100000')
elif lot[0] == mylot[0] and lot[4:7] == mylot[4:7]:
    print('2000')
elif lot[0] == mylot[0] and lot[5:7] == mylot[5:7]:
    print('1000')
elif lot[0] != mylot[0] and lot[4:7] == mylot[4:7]:
    print('200')
elif lot[0] != mylot[0] and lot[5:7] == mylot[5:7]:
    print('100')
elif lot[0] == mylot[0] and lot[2:7] != mylot[2:7]:
    print('20')
else:
    print('0')