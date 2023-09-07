n=int(input())
m=int(input())
s=0
q=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
for j in range(1,m):
    if(m%j==0):
        q=q+j
if(n==q and m==s ):
    print("Amicable")
else:
    print("Not Amicable")
                

        