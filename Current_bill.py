a=int(input())
if a<=199:
    c=1.20
elif a>=200 and a<400:
    c=1.50
elif a>=400 and a<600:
    c=1.80
elif a>600:
    c=2.00
b=a*c
if b>400:
    s=0.15*b
else:
    s=100
cb=b+s
print(F"{cb:.2f}")
