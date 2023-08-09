a=int(input())
b=a//3600
c=(a-(3600*b))//60
d=(a-(3600*b)-(c*60))
print(F"H:M:S-{b}:{c}:{d}")