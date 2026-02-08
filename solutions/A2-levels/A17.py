size,t = map(str,input().split())
topping = input()

m_size = {'S':60,'M':80,'L':100}
t_price = {'P':15,'E':10}
price = m_size[size]

if t == 'T':
        price+=20

if topping[0] != 'N':
    top = topping.split(' ')
    tp = top[0]
    
    if len(top) == 2:
        amount = int(top[1])
    else:
        amount = 1
    
    price += t_price[tp] * amount

print(price)