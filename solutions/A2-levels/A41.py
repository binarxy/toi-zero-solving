# n=int(input()) -- easy way

# print(f"{n:b}")
# print(f"{n:o}")
# print(f"{n:X}")


# normal way

n=int(input())

def convert(num,base):
    if num==0:
        return '0'
    ans=''
    while num>0:
        if base==16: ans+= "0123456789ABCDEF"[num%base]
        else: ans+=str(num%base)
        num//=base

    return ans[::-1]

print(convert(n,2))
print(convert(n,8))
print(convert(n,16))