a=int(input())
b=int(input())
for i in range(a,b+1):
    n=i
    while n:
        r=n%10
        if r==0:
            break
        if i%r!=0:
            break
        n=n//10
    else:
        print(i,end=' ')