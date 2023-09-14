n=int(input())
k=0
q=n
while n>0:
    r=n%10
    k=k*10+r
    n=n//10
if (k==q):
    print("True")
else:
    print("False")