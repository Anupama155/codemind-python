a,b,c=map(int,input().split())
if a>c and b>c:
    print(F"{a+b}")
elif a>b and c>b:
    print(F"{a+c}")
else:
    print(F"{b+c}")