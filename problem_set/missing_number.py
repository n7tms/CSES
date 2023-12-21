n = int(input())
m = set([int(x) for x in input().split()])

o = set(range(1,n+1))
print(*o.difference(m))
