n=int(input())
f=0
while n>0:
    r=n%10
    if(f<r):
        f=r
    n=n//10
print(f)