a=int(input())
if a<=10000:
    b=.8*a
    c=.2*a
elif a<=20000:
    b=.9*a
    c=.25*a
else:
    b=.95*a
    c=.3*a
g=a+b+c
print(F"{g:.2f}")