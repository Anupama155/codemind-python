a=int(input())
flag=False
for i in range(1,a):
    b=i*(i+1)
    if(a==b):
        flag=True
        break
    else:
        flag=False
if flag==True:
    print("YES")
else:
    print("NO")