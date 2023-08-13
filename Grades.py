a,b,c,d,e=map(int,input().split())
g=(a+b+c+d+e)*.2
if g>=90:
    print("Grade A")
elif g>=80:
    print("Grade B")
elif g>=70:
    print("Grade C")
elif g>=60:
    print("Grade D")
elif g>=40:
    print("Grade E")
else:
    print("Grade F")