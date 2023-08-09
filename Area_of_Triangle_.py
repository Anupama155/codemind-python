a,b,c=map(int,input().split())
s=(a+b+c)/2
x=s*(s-a)*(s-b)*(s-c)
ar=x**0.5
print(F"{ar:.2f}")