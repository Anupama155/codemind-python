def rev(a):
    k=0
    t=-a if a<0 else a
    while t:
        r=t%10
        k=k*10+r
        t=t//10
    if(a<0):
        return -k
    else:
        return k
a=int(input())
print(rev(a))
