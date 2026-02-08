info = list(map(str,input().split()))
pos = info[0].upper()
exp = int(info[1])
sal = int(info[2])

bonus = 0
bonus_rate = 0

p_bonus = {
    'M' : 1500,
    'B' : 1000,
    'G' : 500
}

b_rate = {
    'M' : [0.06,0.08,0.10],
    'B' : [0.05,0.06,0.07],
    'G' : [0.04,0.05,0.06]
}

if exp < 5:
    bonus_rate = 0
elif exp < 10:
    bonus_rate = 1
else:
    bonus_rate = 2

bonus = int(p_bonus[pos] + (sal * b_rate[pos][bonus_rate]))

print(bonus)