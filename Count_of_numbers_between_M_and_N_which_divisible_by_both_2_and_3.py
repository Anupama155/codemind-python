a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    if (i%2==0 and i%3==0):
        c=c+1
print(c)