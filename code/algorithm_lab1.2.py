f=open("17.txt")
Sum=0
Mx=0
x=int(f.readline())
for y in f:
    y=int(y)
    if (((x+y)%5==0 and ((x%3==0) or (y%3==0))):
        Sum += 1
        Mx = max(Mx, x+y)
    x=y
print(Sum, Mx)
