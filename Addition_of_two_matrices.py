r = int(input())
mat1=[]
mat2=[]
for a in range(r):
    b=list(map(int,input().split()))
    mat1.append(b)
for c in range(r):
    d=list(map(int,input().split()))
    mat2.append(d)
z=[]
for i in range(r):
    e=[]
    for j in range(r):
        s=(mat1[i][j]+mat2[i][j])
        e.append(s)
    z.append(e)
for x in z:
    for y in x:
        print(y,end=' ')
    print()
