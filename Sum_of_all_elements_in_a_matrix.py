r,c = map(int,input().split())
mat = []
for innerlist in range(r):
    innerlist = list(map(int,input().split()))
    mat.append(innerlist)
s=0
for innerlist in mat:
    for everyvalue in innerlist:
        s=s+everyvalue
print(s)
    