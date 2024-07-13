f=open('9 (2).txt')
cnt=0
for s in f:
    a=[int(x) for x in s.split()]
    kol0=kol1=0
    for i in a:
        kol0+=str(bin(i)[2:]).count('0')
        kol1+=str(bin(i)[2:]).count('1')
    if kol0==kol1:
        cnt+=1
print(cnt)
