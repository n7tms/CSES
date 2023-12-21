s=int(input())
a=list(map(int,input().split()))
m=0
for i,e in enumerate(a[1:],1):
    if e < a[i-1]:
        m += a[i-1]-e
        a[i]=a[i-1]
print(m)
