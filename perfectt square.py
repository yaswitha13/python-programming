import math
n=int(input("enter the number:"))
sqr=math.sqrt(n)
if sqr.is_integer():
    print("perfect square")
else:
    print("not a perfect square")
    
