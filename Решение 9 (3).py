def simple(n):
    return n>1 and all(n%d!=0 for d in range(2,round(n**0.5)+1))
f=open('9 (3).txt')
cnt=0
for s in f:
    a=[int(x) for x in s.split()]
    if all(simple(k)==True for k in a) and len(set(a))==len(a):
        cnt+=1
print(cnt)