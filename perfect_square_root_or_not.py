n=int(input())
f=False
for i in range(n):
    if(i*i==n):
        f=True
        break
    else:
        f=False
if f==True:
    print("True")
else:
    print("False")