r,c = map(int,input().split())
mat = []
for innerlist in range(r):
    innerlist = list(map(int,input().split()))
    mat.append(innerlist)
s=0
s1=0
for innerlist in mat:
    for everyvalue in innerlist:
        if everyvalue%2==0:
            s=s+everyvalue
        else:
            s1=s1+everyvalue
print(s,s1)
    