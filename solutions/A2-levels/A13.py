in1 = input().strip().split()
b,bm = in1[0],int(in1[1])

in2 = input().strip().split()
t,l,v = in2[0],int(in2[1]),int(in2[2])

blist = {'H':5,'O':3,'J':2}
tlist = {'R':(12,18,25),'T':(15,20,30),'M':(10,15,20)}

cal = (tlist[t][l-1]*v) + blist[b]*bm
print(cal)
