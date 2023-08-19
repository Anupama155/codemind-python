a=int(input())
if a<199:
    c=1.20
elif a>=200 and a<400:
    c=1.40
elif a>=400 and a<600:
    c=1.60
elif a>=600 and a<800:
    c=1.80
else:
    c=2.00
b=a*c
if b>400:
    s=0.15*b
else:
    s=0
t=s+b
print(F"Units Consumed: {a}",end='
')
print(F"Cost per Unit: {c:.2f}",end='
')
print(F"Bill: {b:.2f}",end='
')
print(F"Surcharge: {s:.2f}",end='
')
print(F"Total Amount: {t:.2f}")