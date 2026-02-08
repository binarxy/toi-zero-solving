card = input().strip().upper()

fl = {
    'A' : 'ace',
    'Q' : 'queen',
    'J' : 'jack',
    'K' : 'king'
}

sl = {
    'D' : 'diamonds',
    'H' : 'hearts',
    'S' : 'spades',
    'C' : 'clubs'
}

if card[:2] == '10':
    print(f'10 of {sl[card[2]]}')
elif card[0] in '23456789':
    print(f'{card[0]} of {sl[card[1]]}')
else:
    print(f'{fl[card[0]]} of {sl[card[1]]}')
