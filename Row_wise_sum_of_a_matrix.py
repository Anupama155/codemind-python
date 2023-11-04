r,c=map(int,input().split())
mat=[]
for a in range(r):
    l=list(map(int,input().split()))
    mat.append(l)
n=[]
for i in range(r):
    s=0
    for j in range(c):
        s=s+mat[i][j]
    n.append(s)
print(*n)
    