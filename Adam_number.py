a=int(input())
b=a*a
k=0
while a>0:
    r=a%10
    k=k*10+r
    a=a//10
c=k*k
k1=0
while c>0:
    r1=c%10
    k1=k1*10+r1
    c=c//10
if(b==k1):
    print("True")
else:
    print("False")

    