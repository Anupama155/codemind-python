r,c=map(int,input().split())
mat=[]
for a in range(r):
    l=list(map(int,input().split()))
    mat.append(l)
n=[]
for i in range(c):
    s=0
    for j in range(r):
        s=s+mat[j][i]
    n.append(s)
print(*n)
    