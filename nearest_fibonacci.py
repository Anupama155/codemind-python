n = int(input())
x = 0
y = 1
fb = 1
while(fb<n):
    x,y = y,fb
    fb = x+y
if(abs(fb-n) == abs(y-n)):
    print(y,fb)
elif(abs(fb-n) > abs(y-n)):
    print(y)
else:
    print(fb)